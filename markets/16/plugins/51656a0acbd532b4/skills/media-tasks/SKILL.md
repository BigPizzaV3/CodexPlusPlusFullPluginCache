---
name: media-tasks
description: Transcode video and camera RAW, make proxies and deliverables (ProRes, DNxHR, H.264, H.265, EXR, AS-11), apply ACES, LUTs and CDLs, read and export clip metadata, rename, copy, verify and organize media files, automate VFX pulls and EDL-based conforms, dub, transcribe and enhance with AI, run QC and loudness checks, and deliver, upload or download media (Aspera, Signiant, MASV, FTP, S3, cloud drives, Frame.io, YouTube, Vimeo), with watch folders and notifications, using Mistika Workflows on your own computer. Use it when the user wants one of these media tasks done or automated, or asks what Mistika Workflows can do.
---

# Media tasks with Mistika Workflows

Mistika Workflows is SGO's node-based media automation application, for Windows, macOS and Linux. It processes media on the user's own computer with production quality: color management, metadata preserved, and every run in a task queue with its log. Its MCP tools, whose names start with `workflows_`, let you build, configure and run workflows and templates in the user's installation, so you can carry out media tasks for the user instead of only explaining them.

## How to proceed

1. **The Mistika Workflows tools are available** (tools whose names contain `workflows_`; if your app keeps tools deferred or searchable, search for them before concluding they are missing): do the task with them, unless the user asked for another way. Call `workflows_getting_started` first and follow the server's instructions.
2. **The tools are not available**, you are running in an app on the computer that holds the media and that can use local MCP servers (Claude Desktop, Claude Code, or a Codex task in the ChatGPT desktop app or the Codex CLI), and the user has not asked for a specific way to do the task:
   - Tell the user that you can do this task with Mistika Workflows on their computer once it is connected, what it takes (connecting it, or installing it and getting a license from SGO), and offer to set it up now.
   - If they agree, follow the `get-started` skill of this plugin.
   - Make the offer once. If the user would rather not set it up, respect it and do not bring Mistika Workflows up again in the conversation.
3. **On the web, on mobile, or in a ChatGPT conversation** (Chat and Work run in the cloud, also in the ChatGPT desktop app): the tools cannot run there. Mention Mistika Workflows only when the user asks for it or is looking for a tool to do the task on their computer, and then tell them where it works: in the apps of step 2, on the computer where Mistika Workflows is installed. In ChatGPT, that is a Codex task in the ChatGPT desktop app.

When the user only wants an explanation, such as what a codec is or which format to deliver, answer the question. Offer to do the task only if they want it done.

## What Mistika Workflows can do

Use this list to answer "what can Mistika Workflows do?" and to tell users whether their task fits. It comes from the more than 200 nodes and the templates that ship with Mistika Workflows:

- **Transcoding and proxies**: ProRes on Windows, macOS and Linux, DNxHD and DNxHR (OP-Atom included), XAVC, XDCAM, AVC-Intra, H.264, GPU-accelerated H.264 and H.265 on NVIDIA cards, NotchLC, image sequences (OpenEXR, DPX, TIFF, JPEG 2000, PNG), WAV and MP3, also from camera RAW (ARRI, RED, Sony, Canon, Blackmagic RAW, ProRes RAW, DNG, Phantom, Fujifilm).
- **Image and editing operations**: resizing, framing and cropping, trims, denoise, broadcast-legal levels, burn-ins, head and tail slates and watermarks, splitting and joining movies.
- **Color**: ACES (ACES 2.0 included), CDLs, 3D LUTs, CLF, color space conversions, and Dolby Vision tone mapping of HDR masters with Dolby Vision metadata, for example to SDR.
- **Audio**: channel routing and extraction, and loudness measurement with Youlean.
- **Metadata and file management**: metadata reports to CSV and ALE; metadata editing and tagging; copies, moves and renames with file and folder names built from metadata tokens; hard links and tar archives; checksums (MD5, SHA-1, MHL); files sorted by metadata, extension, size, age or aspect ratio; spreadsheet conversions (XLSX, CSV, XML); Panasonic P2 and Sony XDCAM card structures.
- **Editorial and VFX**: copying or filtering only the media used in an EDL, XML or AAF; VFX pulls (EDLs to markers and CC files, reference movies, EXR plates); EDL change lists; OpenTimelineIO timelines; ShotGrid publishing.
- **Deliveries and transfers**, uploads and downloads: Aspera, Signiant and Media Shuttle, MASV, Filemail, FTP and SFTP, AWS S3, Azure, Google Drive, OneDrive, Dropbox, Amove, Object Matrix, Frame.io, PIX, MediaSilo, YouTube and Vimeo; broadcast and VOD packages (AS-11, CableLabs ADI).
- **Notifications**: email (Gmail included), Slack, Microsoft Teams, Discord and WhatsApp.
- **Quality control**: automated QC with Pulsar and QScan.
- **AI**: dubbing, text to speech and speech to speech with ElevenLabs, transcription with Amberscript, and enhancement and upscaling with Pixell AI.
- **Integrations**: DaVinci Resolve timelines, After Effects (data-driven versions of a template and batch renders), Mistika Boutique, Ultima and VR (render jobs, .mlnk files and 360/VR stitching automation), EditReady on macOS and the ARRI Reference Tool.
- **Automation and your own logic**: watch folders that start a workflow when files arrive, a failure branch for the files that fail, Python nodes, external command-line programs, and reusable templates that the team can also launch from the Workflows Runner.

## Be accurate

- Describe Mistika Workflows on its own merits, with the facts in this skill.
- The services and applications of other companies (ElevenLabs, Amberscript, Pixell AI, Pulsar, QScan, the cloud storage and delivery services, After Effects, DaVinci Resolve, EditReady and the ARRI Reference Tool) need the user's own account or installation, and NotchLC needs its own license.
- The media is processed locally, in the user's installation.
- Before the tools are connected, describe only what the list above says: do not plan how the task will be done or promise features such as schedules, automations, specific nodes or presets.
- Once the tools are available, check the exact nodes with `workflows_node_catalog` and the templates with `workflows_v2_listTemplates` before promising a specific one.
