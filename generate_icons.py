#!/usr/bin/env python3
"""
Генератор PWA-иконок для Morse Code Gadget.
Требуется: pip install Pillow
Запуск:    python generate_icons.py
"""
from PIL import Image, ImageDraw
import os

# Палитра приложения
BG           = (10, 12, 16)      # #0a0c10
PCB_DOT      = (28, 34, 40)      # #1c2228
GOLD         = (201, 162, 39)    # #c9a227
GOLD_BRIGHT  = (240, 201, 74)    # #f0c94a


def make_icon(size: int, maskable: bool = False, path: str = "icon.png"):
    """
    Рисует иконку size×size.
    maskable=True → масштабирует логотип в "safe zone" 80%.
    """
    scale = 0.72 if maskable else 0.85
    img = Image.new("RGBA", (size, size), BG)
    draw = ImageDraw.Draw(img)

    # --- PCB-точки на фоне ---
    spacing = max(16, size // 16)
    dot_r   = max(1, size // 220)
    for y in range(0, size, spacing):
        for x in range(0, size, spacing):
            draw.ellipse([x, y, x + dot_r * 2, y + dot_r * 2], fill=PCB_DOT)

    # --- Центр и радиусы ---
    cx, cy = size / 2, size / 2
    R = (size * scale) / 2

    # --- Золотая круглая рамка ---
    frame_w = max(2, int(size * 0.024))
    draw.ellipse([cx - R, cy - R, cx + R, cy + R],
                 outline=GOLD, width=frame_w)

    # --- Внутренний паттерн "· – ·" ---
    inner_R = R - frame_w * 2
    dot_d   = inner_R * 0.30          # диаметр точки
    dash_w  = inner_R * 0.72          # длина тире
    dash_h  = dot_d                   # высота тире = диаметр точки
    gap     = inner_R * 0.14

    total_w = dot_d + gap + dash_w + gap + dot_d
    x0      = cx - total_w / 2
    y       = cy

    # Точка 1
    draw.ellipse([x0, y - dot_d / 2, x0 + dot_d, y + dot_d / 2],
                 fill=GOLD_BRIGHT)
    x0 += dot_d + gap

    # Тире
    draw.rounded_rectangle(
        [x0, y - dash_h / 2, x0 + dash_w, y + dash_h / 2],
        radius=dash_h / 2, fill=GOLD_BRIGHT)
    x0 += dash_w + gap

    # Точка 2
    draw.ellipse([x0, y - dot_d / 2, x0 + dot_d, y + dot_d / 2],
                 fill=GOLD_BRIGHT)

    img.save(path, "PNG", optimize=True)
    print(f"  ✓ {path:38s} ({size}×{size})")


if __name__ == "__main__":
    os.makedirs("icons", exist_ok=True)
    print("Генерация иконок...\n")

    # Обычные
    make_icon(192, path="icons/icon-192.png")
    make_icon(512, path="icons/icon-512.png")
    make_icon(180, path="icons/apple-touch-icon.png")

    # Maskable (с safe zone — для Android adaptive icons)
    make_icon(192, maskable=True, path="icons/icon-maskable-192.png")
    make_icon(512, maskable=True, path="icons/icon-maskable-512.png")

    # Favicon
    make_icon(32, path="icons/favicon-32.png")
    make_icon(16, path="icons/favicon-16.png")

    print("\n✅ Готово! Все файлы в папке ./icons/")