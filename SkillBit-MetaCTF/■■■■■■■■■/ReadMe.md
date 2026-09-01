# ■■■■■■■■■

**Platform:** Skill Bit (previously MetaCTF)

**Description:** Pursuant to the VegetableCTF Files Transparency Act, the government has released records related to the investigation into VegetableCTF, Inc. The release complies with all applicable transparency requirements.

## Approach

The challenge gives us a PDF to download from the website. Opening it, we see a document where the entire body has been covered with black redaction bars.

The question to ask is whether those bars actually removed the text, or whether they are just black rectangles drawn on top of text that is still sitting in the file. Those are two very different things:

- **Real redaction** deletes the underlying text from the PDF and leaves only a black box. The words are gone.
- **Fake redaction** draws a filled black rectangle over the page as a separate drawing object. The text objects underneath are untouched, they are just not visible because something opaque is painted over them.

A PDF is a set of drawing instructions layered on a page, not a flat image, so the second case leaves the original text fully intact and fully extractable.

## Step 1: Test whether the text is still there

The fastest check is to select the entire document with Ctrl+A, copy it, and paste it into any text editor. If the pages were truly redacted you get nothing. If the bars are just drawn on top, the original text comes out in plain readable form.

That is exactly what happens here. The redaction was cosmetic and the full text pastes right out.

## Step 2: Extract it from the command line

Copy and paste works, but pulling the text out with a tool is cleaner and repeatable:

```bash
sudo apt install poppler-utils
pdftotext document.pdf -
```

The trailing `-` prints the extracted text straight to the terminal instead of writing a file. Either way, the flag is sitting in the recovered text.

## Takeaway

This is a real and recurring mistake, not just a CTF gimmick. Improperly redacted PDFs get published by courts, agencies, and companies fairly regularly, and the underlying text is recoverable with nothing more than Ctrl+A and Ctrl+C.

Doing it correctly means removing the content rather than covering it. Tools like Adobe Acrobat's Redact function delete the underlying objects, and flattening the document to an image before publishing also works since it destroys the text layer entirely. Drawing a black box in an image editor or a PDF annotation tool does not.
