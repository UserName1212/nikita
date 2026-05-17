import time, os

width, height = 40, 15
x, y = 1, 1
dx, dy = 1, 1

try:
    while True:
        # Очистка экрана
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Отрисовка кадра
        for r in range(height):
            if r == y:
                print(' ' * x + 'O')
            else:
                print()
                
        # Движение и отскоки
        x += dx
        y += dy
        if x <= 0 or x >= width: dx *= -1
        if y <= 0 or y >= height - 1: dy *= -1
        
        time.sleep(0.05)
except KeyboardInterrupt:
    print("\nАнимация остановлена.")
