// Local preview worker. Compiled with ACE's unchanged sources and resources;
// SlideRasterizer remains the single compositor used by export and the plugin.
import UIKit
import SwiftUI

@main
struct RendererApp: App {
    var body: some Scene {
        WindowGroup {
            Color.clear.task { await RendererJob().renderJob() }
        }
    }
}

@MainActor
private struct RendererJob {
    func renderJob() async {
        let args = ProcessInfo.processInfo.arguments
        guard let flag = args.firstIndex(of: "--render-job"), args.indices.contains(flag + 1),
              let id = UUID(uuidString: args[flag + 1]) else { exit(2) }
        let job = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0]
            .appendingPathComponent("RenderJobs/\(id.uuidString.lowercased())", isDirectory: true)
        do {
            let request = try JSONDecoder().decode(Request.self, from: Data(contentsOf: job.appendingPathComponent("request.json")))
            guard (360...1080).contains(request.width) else { throw Failure("Preview width must be 360…1080") }
            FontRegistrar.registerBundledFonts()
            let assets = job.appendingPathComponent("assets", isDirectory: true)
            try FileManager.default.createDirectory(at: assets, withIntermediateDirectories: true)
            let imported = try CarouselArchive.read(Data(contentsOf: job.appendingPathComponent("input.carousel")), storeAsset: { bytes in
                do {
                    try bytes.write(to: assets.appendingPathComponent(PhotoSource.contentName(for: bytes)), options: .atomic)
                    return true
                } catch { return false }
            })
            guard let document = imported.document, document.unreadLayers.isEmpty,
                  (1...20).contains(document.slides) else { throw Failure("Document is not fully supported by this ACE renderer") }
            let ratio = document.ratio.editorRatio.value
            let slide = CGSize(width: 300, height: 300 / ratio)
            let state = await document.editorState(slide: slide, gap: 0, loadAsset: { asset in
                let name = URL(fileURLWithPath: asset.file).lastPathComponent
                let source = PhotoSource(url: assets.appendingPathComponent(name))
                guard let image = await Task.detached(priority: .userInitiated, operation: {
                    autoreleasepool { source.image(maxPixelSize: 1600) }
                }).value else { return nil }
                return (image, source)
            })
            var warnings: [String] = []
            for missing in state.missing {
                switch missing {
                case .font(let name): warnings.append("Font unavailable; ACE used its native fallback: \(name)")
                default: throw Failure("Native resource is unavailable: \(missing.name)")
                }
            }
            let output = CGSize(width: request.width, height: Int((Double(request.width) / ratio).rounded()))
            let rasterizer = SlideRasterizer(state: state, slide: slide, gap: 0, output: output)
            var slides: [[String: Any]] = []
            for index in 0..<document.slides {
                try autoreleasepool {
                    guard let png = rasterizer.image(index).pngData() else { throw Failure("PNG encoding failed") }
                    let name = String(format: "slide-%02d.png", index + 1)
                    try png.write(to: job.appendingPathComponent(name), options: .atomic)
                    slides.append(["file": name, "slide": index + 1, "width": Int(output.width), "height": Int(output.height)])
                }
            }
            try writeResult(["ok": true, "engine": "ACE SlideRasterizer", "slides": slides, "warnings": warnings], at: job)
            exit(0)
        } catch {
            try? writeResult(["ok": false, "error": String(describing: error)], at: job)
            exit(1)
        }
    }

    private func writeResult(_ value: [String: Any], at job: URL) throws {
        try JSONSerialization.data(withJSONObject: value, options: [.sortedKeys])
            .write(to: job.appendingPathComponent("result.json"), options: .atomic)
    }

    private struct Request: Decodable { let width: Int }
    private struct Failure: Error, CustomStringConvertible {
        let description: String
        init(_ message: String) { description = message }
    }
}
