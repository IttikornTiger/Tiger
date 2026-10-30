"""Compose photo-frame images for the Canva template from the stick-figure PNGs."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Ellipse, FancyBboxPatch, Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "img")
OUT = os.path.join(HERE, "canva")
os.makedirs(OUT, exist_ok=True)
NAVY, TEAL, CORAL, RED = "#1F3B57", "#14A38B", "#E86A50", "#B5121B"


def column(name, title, items, color):
    """Portrait card: header + 3 stacked exercises with labels."""
    f = plt.figure(figsize=(6, 8), dpi=150)
    f.patch.set_facecolor("white")
    ax = f.add_axes([0, 0.9, 1, 0.1]); ax.axis("off")
    ax.add_patch(Rectangle((0, 0), 1, 1, color=color, transform=ax.transAxes))
    ax.text(0.5, 0.5, title, color="white", fontsize=26, weight="bold", ha="center", va="center")
    for i, (img, label, dose) in enumerate(items):
        top = 0.9 - (i + 1) * 0.3
        a = f.add_axes([0.02, top + 0.02, 0.5, 0.27]); a.axis("off")
        a.imshow(mpimg.imread(os.path.join(IMG, img + ".png")))
        t = f.add_axes([0.52, top, 0.46, 0.3]); t.axis("off")
        t.text(0, 0.6, label, fontsize=22, weight="bold", color=NAVY, va="center")
        t.text(0, 0.35, dose, fontsize=16, color="#556575", va="center")
    f.savefig(os.path.join(OUT, name + ".png"), facecolor="white")
    plt.close(f)


column("program_neuro1", "Neuromuscular", [
    ("squat", "Squat", "2-3 sets x 10-15"),
    ("lunge", "Lunge", "2-3 sets x 10-15"),
    ("stepup", "Step-up", "2-3 sets x 10-15")], TEAL)
column("program_neuro2", "Balance & Control", [
    ("singlesquat", "Single-leg\nsquat", "2-3 sets x 10"),
    ("balance", "Wobble board", "30-60 s x 3"),
    ("bike", "Warm-up bike", "~10 min")], NAVY)
column("program_strength", "Strength", [
    ("legpress", "Leg press", "2-3 sets x 8-12 RM"),
    ("kneeext", "Knee\nextension", "2-3 sets x 8-12 RM"),
    ("hamcurl", "Hamstring\ncurl", "2-3 sets x 8-12 RM")], CORAL)


# Knee anatomy schematic with meniscus tear (landscape)
f, ax = plt.subplots(figsize=(10, 6), dpi=150)
f.patch.set_facecolor("white"); ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")
ax.add_patch(FancyBboxPatch((3.6, 3.35), 2.8, 2.6, boxstyle="round,pad=0.25", color="#F1E3C8"))  # femur
ax.add_patch(Ellipse((4.2, 3.3), 1.6, 0.9, color="#F1E3C8")); ax.add_patch(Ellipse((5.8, 3.3), 1.6, 0.9, color="#F1E3C8"))
ax.add_patch(FancyBboxPatch((3.5, 0.2), 3.0, 2.45, boxstyle="round,pad=0.2", color="#F1E3C8"))  # tibia
ax.add_patch(Ellipse((4.2, 2.8), 1.5, 0.35, color=TEAL)); ax.add_patch(Ellipse((5.8, 2.8), 1.5, 0.35, color=TEAL))
ax.plot([5.55, 5.75, 5.6, 5.85], [2.95, 2.8, 2.72, 2.62], color=RED, lw=4)
ax.annotate("Meniscus", xy=(4.0, 2.75), xytext=(0.6, 2.8), fontsize=22, color=TEAL, weight="bold",
            arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=2.5), va="center")
ax.annotate("Degenerative tear", xy=(5.85, 2.75), xytext=(6.9, 1.4), fontsize=20, color=RED, weight="bold",
            arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.5))
ax.text(5, 4.7, "Femur", fontsize=22, ha="center", color=NAVY, weight="bold")
ax.text(5, 1.3, "Tibia", fontsize=22, ha="center", color=NAVY, weight="bold")
f.savefig(os.path.join(OUT, "knee_meniscus.png"), facecolor="white"); plt.close(f)


# Study design flow (landscape)
f, ax = plt.subplots(figsize=(10, 6), dpi=150)
f.patch.set_facecolor("white"); ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")
def node(x, y, w, h, txt, c, fs=18):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.1", color=c))
    ax.text(x, y, txt, color="white", fontsize=fs, ha="center", va="center", weight="bold")
node(5, 5.1, 6.4, 1.0, "140 patients, 35-60 y\nMRI-verified degenerative tear", NAVY)
node(5, 3.6, 2.6, 0.7, "Randomised 1:1", "#556575", 16)
node(2.5, 2.0, 4.0, 1.1, "Exercise therapy\n12 wk (n = 70)", TEAL)
node(7.5, 2.0, 4.0, 1.1, "Partial meniscectomy\n(APM) (n = 70)", CORAL)
node(5, 0.5, 6.4, 0.7, "Follow-up: 3 mo, 12 mo, 2 y", "#556575", 16)
for x2 in (2.5, 7.5):
    ax.annotate("", xy=(x2, 2.6), xytext=(5, 3.25), arrowprops=dict(arrowstyle="-|>", lw=2.5, color="#556575"))
    ax.annotate("", xy=(5, 0.85), xytext=(x2, 1.45), arrowprops=dict(arrowstyle="-|>", lw=2.5, color="#556575"))
ax.annotate("", xy=(5, 3.95), xytext=(5, 4.6), arrowprops=dict(arrowstyle="-|>", lw=2.5, color="#556575"))
f.savefig(os.path.join(OUT, "study_design.png"), facecolor="white"); plt.close(f)


# Results (wide banner) – key numbers
f, ax = plt.subplots(figsize=(16, 5), dpi=150)
f.patch.set_facecolor("white"); ax.set_xlim(0, 16); ax.set_ylim(0, 5); ax.axis("off")
for i, (big, cap, c) in enumerate([
        ("0.9 pts", "KOOS4 difference at 2 y\n95% CI -4.3 to 6.1, P = 0.72", NAVY),
        ("Strength ↑", "Thigh muscle strength better\nin exercise group (3 & 12 mo)", TEAL),
        ("19%", "Exercise group crossed\nover to surgery (13/70)", CORAL)]):
    x = 0.4 + i * 5.2
    ax.add_patch(FancyBboxPatch((x, 0.4), 4.8, 4.2, boxstyle="round,pad=0.1", color=c))
    ax.text(x + 2.4, 3.3, big, color="white", fontsize=44, weight="bold", ha="center", va="center")
    ax.text(x + 2.4, 1.5, cap, color="white", fontsize=19, ha="center", va="center")
f.savefig(os.path.join(OUT, "results.png"), facecolor="white"); plt.close(f)
print(sorted(os.listdir(OUT)))


# Portrait variants for the tall photo frames
def portrait(src, name):
    f = plt.figure(figsize=(6, 8), dpi=150); f.patch.set_facecolor("white")
    a = f.add_axes([0, 0.2, 1, 0.6]); a.axis("off"); a.imshow(mpimg.imread(os.path.join(OUT, src)))
    f.savefig(os.path.join(OUT, name), facecolor="white"); plt.close(f)


# Vertical study flow
f, ax = plt.subplots(figsize=(6, 8), dpi=150)
f.patch.set_facecolor("white"); ax.set_xlim(0, 6); ax.set_ylim(0, 8); ax.axis("off")
def vnode(y, txt, c, h=1.0):
    ax.add_patch(FancyBboxPatch((0.5, y - h / 2), 5, h, boxstyle="round,pad=0.08", color=c))
    ax.text(3, y, txt, color="white", fontsize=17, ha="center", va="center", weight="bold")
vnode(7.2, "140 patients, 35-60 y\nMRI-verified tear", NAVY)
vnode(5.7, "Randomised 1:1", "#556575", 0.7)
ax.add_patch(FancyBboxPatch((0.3, 3.4), 2.6, 1.3, boxstyle="round,pad=0.08", color=TEAL))
ax.text(1.6, 4.05, "Exercise\n12 wk\n(n = 70)", color="white", fontsize=15, ha="center", va="center", weight="bold")
ax.add_patch(FancyBboxPatch((3.1, 3.4), 2.6, 1.3, boxstyle="round,pad=0.08", color=CORAL))
ax.text(4.4, 4.05, "Surgery\nAPM\n(n = 70)", color="white", fontsize=15, ha="center", va="center", weight="bold")
vnode(1.9, "Primary: KOOS4 at 2 y", "#556575", 0.8)
vnode(0.7, "Strength: 3 & 12 mo", "#556575", 0.8)
for x in (1.6, 4.4):
    ax.annotate("", xy=(x, 4.8), xytext=(3, 5.3), arrowprops=dict(arrowstyle="-|>", lw=2.5, color="#556575"))
    ax.annotate("", xy=(3, 2.35), xytext=(x, 3.3), arrowprops=dict(arrowstyle="-|>", lw=2.5, color="#556575"))
ax.annotate("", xy=(3, 6.1), xytext=(3, 6.65), arrowprops=dict(arrowstyle="-|>", lw=2.5, color="#556575"))
f.savefig(os.path.join(OUT, "study_design_portrait.png"), facecolor="white"); plt.close(f)

# Equipment portrait card
f = plt.figure(figsize=(6, 8), dpi=150); f.patch.set_facecolor("white")
a = f.add_axes([0, 0.55, 1, 0.45]); a.axis("off"); a.imshow(mpimg.imread(os.path.join(OUT, "knee_meniscus.png"))[60:820, 180:1420])
items = [("MRI / X-ray", NAVY), ("KOOS questionnaire", TEAL), ("Isokinetic dynamometer", CORAL), ("Hop tests", NAVY)]
for i, (t, c) in enumerate(items):
    b = f.add_axes([0.08, 0.42 - i * 0.12, 0.84, 0.095]); b.axis("off")
    b.add_patch(FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.02", color=c, transform=b.transAxes))
    b.text(0.5, 0.5, t, color="white", fontsize=19, weight="bold", ha="center", va="center")
f.savefig(os.path.join(OUT, "equipment_portrait.png"), facecolor="white"); plt.close(f)
print("portraits ok")


# Landscape exercise strip for the cover
f = plt.figure(figsize=(10, 6), dpi=150); f.patch.set_facecolor("white")
ax = f.add_axes([0, 0.82, 1, 0.18]); ax.axis("off")
ax.add_patch(Rectangle((0, 0), 1, 1, color=TEAL, transform=ax.transAxes))
ax.text(0.5, 0.5, "12-week exercise therapy", color="white", fontsize=28, weight="bold", ha="center", va="center")
for i, (img, lab) in enumerate([("squat", "Squat"), ("lunge", "Lunge"), ("legpress", "Leg press"), ("kneeext", "Knee ext.")]):
    a = f.add_axes([0.01 + i * 0.25, 0.18, 0.23, 0.6]); a.axis("off"); a.imshow(mpimg.imread(os.path.join(IMG, img + ".png")))
    f.text(0.125 + i * 0.25, 0.08, lab, fontsize=20, weight="bold", color=NAVY, ha="center")
f.savefig(os.path.join(OUT, "program_landscape.png"), facecolor="white"); plt.close(f)


# ---- Program cards per Stensrud 2012 appendix (4 rows per card) ----
def column4(name, title, items, color):
    f = plt.figure(figsize=(6, 8), dpi=150); f.patch.set_facecolor("white")
    ax = f.add_axes([0, 0.9, 1, 0.1]); ax.axis("off")
    ax.add_patch(Rectangle((0, 0), 1, 1, color=color, transform=ax.transAxes))
    ax.text(0.5, 0.5, title, color="white", fontsize=24, weight="bold", ha="center", va="center")
    n = len(items); h = 0.88 / n
    for i, (img, label, dose) in enumerate(items):
        top = 0.88 - (i + 1) * h
        a = f.add_axes([0.02, top + 0.01, 0.42, h - 0.02]); a.axis("off")
        a.imshow(mpimg.imread(os.path.join(IMG, img + ".png")))
        t = f.add_axes([0.46, top, 0.52, h]); t.axis("off")
        t.text(0, 0.62, label, fontsize=19, weight="bold", color=NAVY, va="center", linespacing=1.0)
        t.text(0, 0.22, dose, fontsize=15, color="#556575", va="center")
    f.savefig(os.path.join(OUT, name + ".png"), facecolor="white"); plt.close(f)


column4("prog_a", "Warm-up + Neuromuscular", [
    ("bike", "Stationary cycle", "20 min warm-up"),
    ("squat", "Squat", "3 x 10"),
    ("singlesquat", "Single-leg squat", "3 x 10"),
    ("stepup", "Step-up", "3 x 10")], TEAL)
column4("prog_b", "Balance + Plyometric", [
    ("pullloop", "Knee stability\nin pull loop", "3 x 10 (balance pad)"),
    ("skating", "Skating", "3 x 10 (after wk 4)"),
    ("limpingcross", "Limping cross", "3 x 3 rounds (after wk 4)")], NAVY)
column4("prog_c", "Strength (single-leg)", [
    ("legpress", "Leg press", "2-4 x 15 -> 6 (+2)"),
    ("kneeext", "Knee extension", "2-4 x 15 -> 6 (+2)"),
    ("legcurl", "Leg curl", "2-4 x 15 -> 6 (+2)"),
    ("fitball", "Hamstring\non Fitball", "3 x 8")], CORAL)
print("cards ok")
