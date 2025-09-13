import os
import argparse
import tempfile
import shutil
import re
import yaml
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from scripts.pdf.pdf_base import text_to_pdf_from_markdown

OUTPUT_DIRECTORY = "assets/pdfbooks/"


def detect_languages() -> list[str]:
    """Detect language codes from index-*.html files. Includes 'en' for index.html."""
    langs: list[str] = []
    # Always include English
    langs.append("en")
    for fname in os.listdir("."):
        if fname.startswith("index-") and fname.endswith(".html"):
            code = fname[len("index-") : -len(".html")]
            if code and code not in langs:
                langs.append(code)
    return langs


def language_display_name(code: str) -> str:
    mapping = {
        "en": "English",
        "fr": "French",
        "es": "Spanish",
        "ja": "Japanese",
        "zh": "Simplified Chinese",
        "hant": "Traditional Chinese",
        "de": "German",
        "ar": "Arabic",
        "hi": "Hindi",
    }
    return mapping.get(code, code.upper())


def combine_markdown(files: list[str]) -> str:
    """Read, strip front matter, normalize image tags, and concatenate two files."""
    combined_content = ""
    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            # Remove YAML front matter
            front_matter = ""
            match = re.search(r"^---(.*?)---", content, re.DOTALL)
            if match:
                front_matter = match.group(1)
                content = content[match.end() :]

            file_title = os.path.splitext(os.path.basename(file_path))[0]
            try:
                if front_matter:
                    yaml_data = yaml.safe_load(front_matter)
                    if isinstance(yaml_data, dict) and "title" in yaml_data:
                        file_title = str(yaml_data["title"])  # best-effort
            except yaml.YAMLError as e:
                print(f"Error parsing YAML in {file_path}: {e}")

            combined_content += f"# {file_title}\n"

            if "](assets" in content:

                def replace_image_tag(m):
                    if m:
                        image_tag = m.group(0)
                        image_url_match = re.search(r"\((.*?)\)", image_tag)
                        if image_url_match:
                            image_url = image_url_match.group(1)
                            return f"![]({image_url})"
                        return image_tag
                    return ""

                # Handle centered images with optional captions
                def replace_centered_image(m):
                    if m:
                        image_tag = m.group(1)
                        return replace_image_tag(re.search(r"(!\[.*?\])", image_tag))
                    return ""

                content, _ = re.subn(
                    r"{:\s*\.centered\s*}\s*(!\[.*?\])(\s*\*.*?\*{:\s*\.caption\s*})?",
                    replace_centered_image,
                    content,
                )

                # Handle responsive images
                content = re.sub(
                    r"(!\[.*?\]){:\s*\.responsive\s*}",
                    lambda m: replace_image_tag(m) if m else "",
                    content,
                )

                # Remove captions
                content, _ = re.subn(r"\*.*?\*{:\s*\.caption\s*}", "", content)

            combined_content += content
            combined_content += "\n\n"
    return combined_content


def build_pdf_for_language(lang: str, output_dir: str) -> None:
    os.makedirs(output_dir, exist_ok=True)

    # Helper: first existing path in list
    def pick(existing_paths: list[str]) -> str | None:
        for p in existing_paths:
            if os.path.exists(p):
                return p
        return None

    # Build sources
    sources: list[str] = []

    # Always prefer resume if present
    resume_path = pick(
        [
            f"_posts/{lang}/2025-01-11-resume-{lang}.md",
            f"original/2025-01-11-resume-{lang}.md",
        ]
    )
    if resume_path:
        sources.append(resume_path)

    if lang == "en":
        # Custom English bundle: add selected originals and explicitly drop portfolio
        english_candidates = [
            "original/2025-08-24-recommend-for-engineers-en.md",
            "original/2025-08-24-links-en.md",
            "original/2025-08-18-llm-en.md",
            "original/2025-07-27-engineering-optimized-ai-en.md",
            "original/2025-02-15-english-en.md",
            "original/2025-07-10-english-animation-en.md",
            "original/2024-11-29-vision-tips-en.md",
            "original/2024-12-10-life-tips-en.md",
            "original/2025-01-17-investing-en.md",
        ]
        # Append only those that exist
        for p in english_candidates:
            if os.path.exists(p):
                sources.append(p)
        # Do NOT include any portfolio file for English
    else:
        # Default: require resume + portfolio for non-English
        portfolio_path = pick(
            [
                f"_posts/{lang}/2025-01-11-portfolio-{lang}.md",
                f"original/2025-01-11-portfolio-{lang}.md",
            ]
        )
        if portfolio_path:
            sources.append(portfolio_path)
        # Enforce both resume and portfolio for non-English
        if len(sources) != 2:
            expected = [
                f"_posts/{lang}/2025-01-11-resume-{lang}.md | original/2025-01-11-resume-{lang}.md",
                f"_posts/{lang}/2025-01-11-portfolio-{lang}.md | original/2025-01-11-portfolio-{lang}.md",
            ]
            print(
                f"Skip {lang}: missing files. Expected any of each pair:\n- {expected[0]}\n- {expected[1]}"
            )
            return

    # Ensure we have something to build
    if not sources:
        print(f"Skip {lang}: no source files found (resume and/or selected originals).")
        return


    try:
        tmpdir = tempfile.mkdtemp(prefix=f"epubpdf-{lang}-")
        combined_md_path = os.path.join(tmpdir, f"lzwjava-essays-{lang}.md")
        with open(combined_md_path, "w", encoding="utf-8") as tmp_file:
            tmp_file.write(combine_markdown(sources))

        # PDF (xelatex via pdf_base)
        print(f"Converting to PDF ({language_display_name(lang)}): lzwjava-essays-{lang}.pdf")
        output_pdf_file = os.path.join(output_dir, f"lzwjava-essays-{lang}.pdf")
        try:
            ok = text_to_pdf_from_markdown(
                input_markdown_path=combined_md_path,
                output_pdf_path=output_pdf_file,
                dry_run=False,
            )
            if ok:
                print(f"Wrote {output_pdf_file}")
        except Exception as e:
            print(f"Error converting to {output_pdf_file}: {e}")
    except Exception as e:
        print(f"Error processing {lang}: {e}")
    finally:
        if 'tmpdir' in locals() and os.path.isdir(tmpdir):
            shutil.rmtree(tmpdir, ignore_errors=True)


def main():
    parser = argparse.ArgumentParser(description="Build 2-file PDF across languages.")
    parser.add_argument(
        "-o",
        "--output_dir",
        help="Output directory for the generated PDF files.",
        default=OUTPUT_DIRECTORY,
    )
    parser.add_argument(
        "--langs",
        nargs="*",
        help="Optional list of language codes to build (default: detected).",
    )
    args = parser.parse_args()

    langs = args.langs if args.langs else detect_languages()
    # Keep at most 9 languages if more are present
    if len(langs) > 9:
        langs = langs[:9]

    print(f"Languages: {', '.join(langs)}")
    for lang in langs:
        build_pdf_for_language(lang, args.output_dir)


if __name__ == "__main__":
    main()
