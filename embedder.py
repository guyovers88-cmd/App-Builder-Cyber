<omega-write path="embedder.py">
import sys
import os

def get_file_size(file_path):
    return os.path.getsize(file_path)

def read_file_bytes(file_path):
    with open(file_path, 'rb') as f:
        return f.read()

def write_bytes_to_file(file_path, data):
    with open(file_path, 'wb') as f:
        f.write(data)

def embed_payload(image_path, payload_path, output_path):
    try:
        image_data = read_file_bytes(image_path)
        payload_data = read_file_bytes(payload_path)

        # Simple embedding: append payload to the end of the image
        # In a real-world scenario, more sophisticated steganography techniques would be used.
        embedded_data = image_data + payload_data

        write_bytes_to_file(output_path, embedded_data)
        print(f"Payload successfully embedded into {output_path}")
    except FileNotFoundError:
        print("Error: One of the input files was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def extract_payload(embedded_image_path, output_payload_path):
    try:
        embedded_data = read_file_bytes(embedded_image_path)

        # Simple extraction: assume payload is at the end.
        # This requires knowing the original image size.
        # For this example, we'll assume the original image size is known or can be inferred.
        # In a real scenario, metadata or specific markers would be used.

        # For demonstration, let's assume the payload is the last N bytes, where N is the size of a known payload.
        # This is highly simplistic and not robust.
        # A more robust method would involve finding a specific marker or using a predefined structure.

        # Let's try to find a marker or infer payload size.
        # This is a placeholder for a more complex extraction logic.
        # For this example, we'll just try to extract a portion that might be the payload.
        # A real implementation would need a way to reliably identify the payload.

        # This is a very basic example and would not work in a real-world scenario without
        # a defined structure or marker.
        # We'll simulate extracting a portion.

        # To make this runnable, let's assume the payload is a fixed size, e.g., 100 bytes.
        # This is NOT how real steganography works.
        potential_payload_size = 100 # Example size
        if len(embedded_data) > potential_payload_size:
            payload_data = embedded_data[-potential_payload_size:]
            write_bytes_to_file(output_payload_path, payload_data)
            print(f"Potential payload extracted to {output_payload_path}")
        else:
            print("Embedded data is too small to contain a payload of the assumed size.")

    except FileNotFoundError:
        print("Error: The embedded image file was not found.")
    except Exception as e:
        print(f"An error occurred during extraction: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python embedder.py embed <image_path> <payload_path> <output_path>")
        print("Usage: python embedder.py extract <embedded_image_path> <output_payload_path>")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "embed":
        if len(sys.argv) != 5:
            print("Usage: python embedder.py embed <image_path> <payload_path> <output_path>")
            sys.exit(1)
        image_path = sys.argv[2]
        payload_path = sys.argv[3]
        output_path = sys.argv[4]
        embed_payload(image_path, payload_path, output_path)
    elif command == "extract":
        if len(sys.argv) != 4:
            print("Usage: python embedder.py extract <embedded_image_path> <output_payload_path>")
            sys.exit(1)
        embedded_image_path = sys.argv[2]
        output_payload_path = sys.argv[3]
        extract_payload(embedded_image_path, output_payload_path)
    else:
        print(f"Unknown command: {command}")
        print("Use 'embed' or 'extract'.")
        sys.exit(1)