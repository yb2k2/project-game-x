    import tkinter as tk
    
    def start_game():
        print("Game started!")
    
    def quit_game():
        root.destroy()
    
    root = tk.Tk()
    root.title("My Game")
    
    start_button = tk.Button(root, text="Bắt đầu game", command=start_game)
    start_button.pack(pady=10)
    
    quit_button = tk.Button(root, text="Thoát Game", command=quit_game)
    quit_button.pack(pady=10)
    
    root.mainloop() 