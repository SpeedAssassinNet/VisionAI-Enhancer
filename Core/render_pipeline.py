class RenderPipeline:

    def start_render(self):
        return "Render process started"

    def export_video(self):
        return "Export complete"


pipeline = RenderPipeline()

print(pipeline.start_render())
