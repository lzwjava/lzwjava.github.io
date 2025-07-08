.PHONY: latex audio-pipeline pdf-pipeline clean copy

CC = xelatex
EXAMPLES_DIR = latex
RESUME_EN_DIR = latex/en/resume-en
RESUME_ZH_DIR = latex/zh/resume-zh
COVER_LETTER_DIR = latex/coverletter
INTRODUCTION_DIR = latex/en
INTRODUCTION_ZH_DIR = latex/zh
RESUME_SRCS = $(shell find $(RESUME_EN_DIR) -name '*.tex')
RESUME_ZH_SRCS = $(shell find $(RESUME_ZH_DIR) -name '*.tex')
INTRODUCTION_SRCS = $(shell find $(INTRODUCTION_DIR) -name '*.tex')
INTRODUCTION_ZH_SRCS = $(shell find $(INTRODUCTION_ZH_DIR) -name '*.tex')


# Existing latex target
latex: $(foreach x, coverletter coverletter-zh resume-zh resume, $x.pdf)

resume-en.pdf: $(RESUME_EN_DIR)/resume-en.tex $(RESUME_SRCS)
	$(CC) -output-directory=$(RESUME_EN_DIR) $<

resume-en-dark.pdf: $(RESUME_EN_DIR)/resume-en-dark.tex $(RESUME_SRCS)
	$(CC) -output-directory=$(RESUME_EN_DIR) $<

resume-zh.pdf: $(RESUME_ZH_DIR)/resume-zh.tex $(RESUME_ZH_SRCS)
	$(CC) -output-directory=$(RESUME_ZH_DIR) $<

coverletter.pdf: $(COVER_LETTER_DIR)/coverletter.tex
	$(CC) -output-directory=$(COVER_LETTER_DIR) $<

coverletter-zh.pdf: $(COVER_LETTER_DIR)/coverletter-zh.tex
	$(CC) -output-directory=$(COVER_LETTER_DIR) $<

introduction-en.pdf: $(INTRODUCTION_DIR)/introduction-en.tex
	$(CC) -output-directory=$(INTRODUCTION_DIR) $<

introduction-zh.pdf: $(INTRODUCTION_ZH_DIR)/introduction-zh.tex
	$(CC) -output-directory=$(INTRODUCTION_ZH_DIR) $<	

# New audio-pipeline target
audio-pipeline:
	python audio-pipeline.py --task posts --n 10

# New pdf-pipeline target
pdf-pipeline:
	python pdf-pipeline.py --task posts --n 10

pipelines: audio-pipeline pdf-pipeline

introductions: introduction-en.pdf introduction-zh.pdf

# Clean target to remove generated files
clean:
	rm -rf $(EXAMPLES_DIR)/*.pdf

copy:
	mkdir -p assets/resume

	cp $(RESUME_EN_DIR)/resume-en.pdf assets/resume/Zhiwei.Li.Resume.pdf
	cp $(RESUME_EN_DIR)/resume-en-dark.pdf assets/resume/Zhiwei.Li.Resume.Dark.pdf
	cp $(RESUME_ZH_DIR)/resume-zh.pdf assets/resume/Zhiwei.Li.Resume.ZH.pdf

copy-introduction:
	cp latex/en/introduction-en.pdf assets/resume/Zhiwei.Li.Introduction.EN.pdf
	cp latex/zh/introduction-zh.pdf assets/resume/Zhiwei.Li.Introduction.ZH.pdf