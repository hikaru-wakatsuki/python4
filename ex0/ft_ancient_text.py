from typing import TextIO


def ft_ancient_text() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    text: str = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {text}")
    try:
        f: TextIO = open(text, "r")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        return
    print("Connection established...")
    print()
    try:
        print("RECOVERED DATA:")
        print(f.read())
    except Exception:
        print("ERROR: Failed to read data from storage vault.")
        return
    finally:
        f.close()
    print()
    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    ft_ancient_text()
