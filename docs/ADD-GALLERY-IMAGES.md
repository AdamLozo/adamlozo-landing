# Add images to the gallery

The gallery page is `gallery/index.html`. It loads `gallery/gallery.json` and shows the images in a random order. There is no build step for the site. Render deploys the site when you push to `main`.

## Files

| File | Purpose |
|---|---|
| `C:\Claude\Projects\Gallery\Images` | Source folder for the images. |
| `C:\Claude\Projects\Gallery\Midjourney-Prompt-Index.md` | Prompts for the source images, and the "Not mine" list. |
| `tools/build_gallery.py` | Makes the web images and updates `gallery/gallery.json`. |
| `tools/gallery_config.json` | Exclusions, retouch boxes, and crops. |
| `C:\Claude\Projects\Gallery\Retouched` | Retouched copies of source images, with the same file names. The build script uses them instead of the sources. |
| `gallery/gallery.json` | One entry for each image, with the captions. |
| `gallery/version.txt` | Short hash of `gallery.json`. The build script writes it. The page uses it to load the newest `gallery.json` after a deploy. |
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
2. Every image in the source folder is Adam's work, except file names in the 'Not mine' list in `Midjourney-Prompt-Index.md`. Exclude those images.
3. Match each new image to its prompt in `Midjourney-Prompt-Index.md`. If Adam wrote a title next to a prompt in the index, use that title exactly.
4. Fill in the four text fields in `gallery/gallery.json`. Obey these rules:
   - `title`: 2 to 5 words.
   - `style`: `After <Artist Name>` only when the prompt names an artist. Otherwise, use an empty string.
   - `description`: 1 to 2 sentences, 35 words maximum.
   - `alt`: a plain description of what the image shows.
   - Do not copy prompt text into a caption.
   - Do not invent facts.
   - Do not use the words "AI" or "Midjourney" in a caption.
5. Delete the previews.

### 4. Signatures, logos, and mastheads

Examine each new preview for marks. Examine the corners and the edges closely. Obey these rules:

- If an image shows a real artist signature, remove it with `retouch` boxes. Do not crop. If the retouch leaves a visible trace, exclude the image.
- If an image shows a real logo or real masthead, exclude it.
- Keep images with scribbles or generic fake lettering. Do not crop or retouch them.

To retouch a signature, use Photoshop first. It matches the texture better than `cv2.inpaint`:

1. Open the source image in Photoshop. Select a rectangle that covers each signature. Run Generative Remove.
2. Export a PNG with the same file name to `C:\Claude\Projects\Gallery\Retouched`. Close the document without saving. Do not change the source file.
3. Run the build script. If a file with the same name is in `Retouched`, the script uses it instead of the source and stores `"retouched": true` in the entry.
4. Check the result with the same pass rules as below.

If Photoshop is not available, use `retouch` boxes:

1. Add `retouch` boxes for the image `id` to `tools/gallery_config.json`. Each box is a rectangle in fractions of the source image. `left` and `top` are the start. `right` and `bottom` are the end. An entry can have more than one box:

   ```json
   "retouch": {
     "<id>": [{"left": 0.06, "top": 0.90, "right": 0.21, "bottom": 0.94}]
   }
   ```

   - Use the smallest boxes that cover each signature fully.
   - The script expands each box by a few pixels and fills it with `cv2.inpaint` (Telea). The source file does not change.
2. Run the build script again. It rebuilds each image whose `retouch` boxes changed.
3. Make a 512 px preview of the image and a 512 px close crop of each retouched area.
4. The retouch passes only if all of these are true:
   - No letter or part of a letter is visible.
   - The filled area matches the texture and color around it, with no visible smear or blur patch.
   - The retouch does not touch a person, face, or hand.
5. If the retouch does not pass after 2 attempts, exclude the image.

To exclude an image, add its source file name to `exclude`. The build script removes its entry and its web images:

```json
"exclude": ["<source file name>"]
```

The script also supports `crops`, but use a crop only if Adam asks for one.

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
2. Push to `main`. Render deploys the site in approximately 30 seconds to 3 minutes.
3. Open `https://adamlozo.com/gallery/` and make sure that the new images show.
