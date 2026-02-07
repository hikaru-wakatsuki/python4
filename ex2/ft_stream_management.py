import sys


def ft_stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    archivist_id: str = input("Input Stream active. Enter archivist ID: ")
    status_report: str = input("Input Stream active. Enter status report: ")
    print()
    sys.stdout.write(f"[STANDARD] Archive status from "
                     f"{archivist_id}: {status_report}\n")
    sys.stderr.write("[ALERT] System diagnostic: "
                     "Communication channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    print()
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    ft_stream_management()
