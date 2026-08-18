import subprocess

def download_audio(query, output_dir="downloads"):
    subprocess.run([
        "spotdl", "download", query,
        "--output", f"{output_dir}/{{artists}} - {{title}}.{{output-ext}}",
        "--cookies-from-browser", "firefox"
    ])
