from PIL import Image, ImageDraw
import json

def rebuild_sprite(json_data, texture_path):
    canvas_width = json_data["Canvas"]["Width"]
    canvas_height = json_data["Canvas"]["Height"]
    sprite = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 0))

    for block in json_data["Block"]:

        for mesh in block["Mesh"]:
            tex_no = mesh["texNo"]
            src_offset_x = mesh["srcOffsetX"]
            src_offset_y = mesh["srcOffsetY"]
            tex_u1 = mesh["texU1"]
            tex_v1 = mesh["texV1"]
            tex_u2 = mesh["texU2"]
            tex_v2 = mesh["texV2"]
            view_x = mesh["viewX"]
            view_y = mesh["viewY"]

            texture = Image.open(texture_path).convert("RGBA")

            cropped_texture = texture.crop((
                round(tex_u1 * texture.width),
                round(tex_v1 * texture.height),
                round(tex_u2 * texture.width),
                round(tex_v2 * texture.height)
            ))

            sprite.paste(cropped_texture, (round(src_offset_x), round(src_offset_y)), cropped_texture)

    return sprite

with open(f'atlas.json', "r") as json_file:
    json_data = json.load(json_file)

resulting_sprite = rebuild_sprite(json_data, f"tex0.png")
resulting_sprite.save("sprite.png", "PNG")
