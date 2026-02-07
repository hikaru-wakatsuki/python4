from typing import TextIO


def ft_ancient_text() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    text: str = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {text}")
    print("Connection established...")
    print()
    try:
        f: TextIO = open(text)
        print(f.read())
        f.close()
        print("Data recovery complete. Storage unit disconnected.")
    except Exception:
        print("ERROR: Storage vault not found.  Run data generator first.")


if __name__ == "__main__":
    ft_ancient_text()
