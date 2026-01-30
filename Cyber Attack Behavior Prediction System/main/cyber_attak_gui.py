import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.preprocessing import LabelEncoder
import warnings

# SUPPRESS SKLEARN WARNING
warnings.filterwarnings("ignore", message="X has feature names, but RandomForestClassifier was fitted without feature names")

# LOAD TRAINED MODEL
rf_model = joblib.load("cyber_attack_model.pkl")

TRAINING_FEATURES = [
    "Source Port",
    "Destination Port",
    "Protocol",
    "Packet Length",
    "Flag"
]

data_df = None
prediction_done = False

# GUI SETUP
root = tk.Tk()
root.title("Cyber Attack Prediction System")
root.geometry("1200x780")
root.configure(bg="#0b0b0b")

tk.Label(
    root,
    text="Cyber Attack Prediction System",
    font=("Courier New", 22, "bold"),
    fg="#00ff00",
    bg="#0b0b0b"
).pack(pady=10)

btn_frame = tk.Frame(root, bg="#0b0b0b")
btn_frame.pack(pady=8)

def neon_button(text, command, col):
    tk.Button(
        btn_frame,
        text=text,
        command=command,
        font=("Courier New", 12, "bold"),
        bg="#00ff00",
        fg="black",
        width=22
    ).grid(row=0, column=col, padx=6)

# CSV PREVIEW
preview = tk.Text(
    root, height=7,
    bg="#111111", fg="#00ff00",
    font=("Consolas", 11)
)
preview.pack(fill="x", padx=20)
preview.insert("end", "Load dataset to begin...")
preview.config(state="disabled")

# TABLE
table_frame = tk.Frame(root)
table_frame.pack(fill="both", expand=True, padx=20, pady=5)

tree = ttk.Treeview(table_frame, show="headings")
tree.pack(side="left", fill="both", expand=True)

scroll = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scroll.set)
scroll.pack(side="right", fill="y")

# PLOT FRAME
plot_frame = tk.Frame(root, bg="#0b0b0b", height=150)
plot_frame.pack(fill="x", padx=20, pady=5)

# GLOBAL FLAGS FOR TOGGLE
feature_graph_visible = False
attack_graph_visible = False

# LOAD CSV
def load_csv():
    global data_df, prediction_done
    prediction_done = False

    path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if not path:
        return

    data_df = pd.read_csv(path)

    preview.config(state="normal")
    preview.delete(1.0, "end")
    preview.insert("end", str(data_df.head()))
    preview.config(state="disabled")

    messagebox.showinfo("Success", "Dataset loaded successfully")

# PREDICT ATTACK
def predict_attack():
    global data_df, prediction_done

    if data_df is None:
        messagebox.showwarning("Error", "Load dataset first")
        return

    X = pd.DataFrame()
    for col in TRAINING_FEATURES:
        if col not in data_df.columns:
            X[col] = 0
        elif data_df[col].dtype == object:
            le = LabelEncoder()
            X[col] = le.fit_transform(data_df[col].astype(str))
        else:
            X[col] = pd.to_numeric(data_df[col], errors="coerce").fillna(0)

    X = X[TRAINING_FEATURES]

    predictions = rf_model.predict(X)
    data_df["Prediction"] = predictions
    prediction_done = True

    # Display table
    tree.delete(*tree.get_children())
    tree["columns"] = list(data_df.columns)
    for c in data_df.columns:
        tree.heading(c, text=c)
        tree.column(c, width=140)
    for _, row in data_df.iterrows():
        tree.insert("", "end", values=list(row))

    messagebox.showinfo("Done", "Prediction completed successfully")


# FEATURE IMPORTANCE TOGGLE 

def show_feature_importance():
    global feature_graph_visible, attack_graph_visible
    if not prediction_done:
        messagebox.showwarning("Error", "Predict first")
        return

    if attack_graph_visible:
        for w in plot_frame.winfo_children():
            w.destroy()
        attack_graph_visible = False

    if feature_graph_visible:
        for w in plot_frame.winfo_children():
            w.destroy()
        feature_graph_visible = False
        return

    for w in plot_frame.winfo_children():
        w.destroy()

    importance = rf_model.feature_importances_
    fig, ax = plt.subplots(figsize=(4,3), facecolor="#0b0b0b")  # smaller figure

    bars = ax.barh(TRAINING_FEATURES, importance, color="#00ff00", edgecolor="#00ff00")
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 0.002, bar.get_y() + bar.get_height()/2, f"{width:.2f}",
                ha='left', va='center', color="#00ff00", fontsize=9, fontweight='bold')

    ax.set_title("Feature Importance", color="#00ff00", fontsize=12, fontweight='bold')
    ax.set_xlabel("Importance Score", color="#00ff00", fontsize=10, fontweight='bold')
    ax.set_ylabel("Features", color="#00ff00", fontsize=10, fontweight='bold')

    ax.tick_params(axis='x', colors="#00ff00", labelsize=9)
    ax.tick_params(axis='y', colors="#00ff00", labelsize=9)
    ax.spines['bottom'].set_color("#00ff00")
    ax.spines['left'].set_color("#00ff00")
    ax.spines['top'].set_color("#0b0b0b")
    ax.spines['right'].set_color("#0b0b0b")

    plt.tight_layout()
    canvas = FigureCanvasTkAgg(fig, plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="x", expand=False)

    feature_graph_visible = True

# ATTACK DISTRIBUTION TOGGLE
def show_attack_distribution():
    global attack_graph_visible, feature_graph_visible
    if not prediction_done:
        messagebox.showwarning("Error", "Run prediction first")
        return

    if feature_graph_visible:
        for w in plot_frame.winfo_children():
            w.destroy()
        feature_graph_visible = False

    if attack_graph_visible:
        for w in plot_frame.winfo_children():
            w.destroy()
        attack_graph_visible = False
        return

    for w in plot_frame.winfo_children():
        w.destroy()

    counts = data_df["Prediction"].value_counts()
    fig, ax = plt.subplots(figsize=(2,3), facecolor="#0b0b0b")  # smaller figure

    ax.bar(["Benign", "Attack"], [counts.get(0,0), counts.get(1,0)], color="#00ff00")
    ax.set_title("Attack Distribution", color="#00ff00", fontsize=12, fontweight='bold')
    ax.set_ylabel("Number of Samples", color="#00ff00", fontsize=10, fontweight='bold')
    ax.set_xlabel("Prediction", color="#00ff00", fontsize=10, fontweight='bold')

    ax.tick_params(axis='x', colors="#00ff00", labelsize=9)
    ax.tick_params(axis='y', colors="#00ff00", labelsize=9)
    ax.spines['bottom'].set_color("#00ff00")
    ax.spines['left'].set_color("#00ff00")
    ax.spines['top'].set_color("#0b0b0b")
    ax.spines['right'].set_color("#0b0b0b")

    plt.tight_layout()
    canvas = FigureCanvasTkAgg(fig, plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="x", expand=False)

    attack_graph_visible = True

# ROW CLICK → FULL DETAILS
def on_row_click(event):
    selected = tree.focus()
    if not selected:
        return
    values = tree.item(selected, "values")
    row_data = dict(zip(tree["columns"], values))
    result = "⚠ ATTACK DETECTED\n\n" if int(row_data["Prediction"]) == 1 else "✅ BENIGN TRAFFIC\n\n"
    details = "\n".join(f"{k}: {v}" for k, v in row_data.items())
    messagebox.showinfo("Prediction Result", result + details)

tree.bind("<Double-1>", on_row_click)

# BUTTONS
neon_button("Load Dataset", load_csv, 0)
neon_button("Predict Attack", predict_attack, 1)
neon_button("Attack Distribution", show_attack_distribution, 2)
neon_button("Feature Importance", show_feature_importance, 3)

root.mainloop()
