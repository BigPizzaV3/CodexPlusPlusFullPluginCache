# ACE Carousel Creator

Create an editable carousel from a brief, exact slide copy or selected photographs. Download the `.carousel` project and open it in ACE using **Projects → Import** or **Templates → Import**.

The public plugin connects to [Carousel Creator MCP](https://mcp.quokka.software/mcp). It supports 1–20 slides, native photo grids and frames, text, shapes, masks and blending. The skill reads the writing guide when composing copy and checks the layout before packaging it.

Use supported ChatGPT file references for attachments. For a photo selected on your computer, a client with filesystem access can upload it to a temporary URL from `prepare_photo_upload`. Only share files selected for this project. Keep upload links and IDs private. Project download links expire after one hour and can expire earlier if the server restarts.

The public server returns the editable project. On a Mac with the ACE native renderer configured, `create_carousel` and `render_carousel` can also return PNG previews. The connected server reports its capabilities in `get_carousel_spec` under `overview`.
