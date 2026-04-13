import time

def train():
    print("Starting training process...")

    # Simulate epochs
    for epoch in range(3):
        print(f"Epoch {epoch+1}/3...")
        time.sleep(1)

    print("Training completed successfully!")

if __name__ == "__main__":
    train()