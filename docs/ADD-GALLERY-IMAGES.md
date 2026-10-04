# Add images to the gallery

The gallery page is `gallery/index.html`. It loads `gallery/gallery.json` and shows the images in a random order. There is no build step for the site. Render deploys the site when you push to `main`.

## Files

| File | Purpose |
|---|---|
| `C:\Users\adam\OneDrive\Pictures\Website Images` | Source folder for the images. |
| `Midjourney-Prompt-Index.md` (in the source folder) | Prompts for the source images. |
| `tools/build_gallery.py` | Makes the web images and updates `gallery/gallery.json`. |
| `tools/gallery_config.json` | Crops and exclusions. |
| `gallery/gallery.json` | One entry for each image, with the captions. |
| `gallery/images/display/<id>.webp` | Grid image. Long edge 1600 px. |
| `gallery/images/full/<id>.jpg` | Lightbox image. Long edge max 3000 px. |

## Procedure

### 1. Add the source images

1. Put the new images in the source folder.
2. Add their prompts to `Midjourney-Prompt-Index.md`.

### 2. Run the build script

```bash
python tools/build_gallery.py
```

The script makes the web images for new sources only. It adds a new entry with empty `title`, `style`, `description`, and `alt` fields. It never changes the text of an existing entry.

### 3. Write the captions

1. Make a 512 px preview of each new image in `%TEMP%`. Do not view the full-size images.
2. Before you write captions, list each new image with its file name and a short description. Ask Adam to confirm that he made each image. Exclude each image that he did not make.
3. Match each new image to its prompt in `Midjourney-Prompt-Index.md`.
4. Fill in the four text fields in `gallery/gallery.json`. Obey these rules:
   - `title`: 2 to 5 words.
   - `style`: `After <Artist Name>` only when the prompt names an artist. Otherwise, use an empty string.
   - `description`: 1 to 2 sentences, 35 words maximum.
   - `alt`: a plain description of what the image shows.
   - Do not copy prompt text into a caption.
   - Do not invent facts.
   - Do not use the words "AI" or "Midjourney" in a caption.
5. Delete the previews.

### 4. Remove fake signatures, logos, and mastheads

1. Examine each new preview for a fake signature, a logo, or magazine masthead text. Examine the corners and the edges closely.
2. To remove a mark, add a crop for the image `id` to `tools/gallery_config.json`. The values are fractions of the source image to remove from each side:

   ```json
   "crops": {
     "<id>": {"left": 0.0, "top": 0.0, "right": 0.0, "bottom": 0.06}
   }
   ```

   - Use the smallest crop that removes the mark fully.
   - Crop one or two sides only.
3. If a crop must remove more than 15% of the width or height, or cuts into the main subject, exclude the image. Add its source file name to `exclude`:

   ```json
   "exclude": ["<source file name>"]
   ```

4. Run the build script again. It rebuilds each image whose crop changed. It removes the entry and the web images of each excluded source.
5. Make a new 512 px preview of each cropped image. Make sure that no mark is visible.

To rebuild one image, use this command:

```bash
python tools/build_gallery.py --force <id>
```

### 5. Test locally

1. Start a local server from the repo root:

   ```bash
   python -m http.server 8000
   ```

2. Open `http://localhost:8000/gallery/`.
3. Make sure that the new images show, the captions are correct, and the lightbox works.
4. Make sure that the browser console shows no errors.
5. Stop the server.

### 6. Commit and push

1. Commit the changes on `main`: `gallery/`, `tools/gallery_config.json`, and any changed docs.
2. Push to `main`. Render deploys the site in approximately 3 minutes.
3. Open `https://adamlozo.com/gallery/` and make sure that the new images show.
