import bpy

bpy.context.preferences.addons["ZenUV"].preferences.td_im_size_presets = "4096"
bpy.context.preferences.addons["ZenUV"].preferences.TexelDensity = 4000

bpy.context.object.data.uv_layers["UVMap"].name = "uv_fabrics"
bpy.ops.mesh.uv_texture_add()
bpy.context.object.data.uv_layers["UVMap"].name = "uv_maps"

bpy.context.object.data.uv_layers['uv_fabrics'].active = True 
bpy.ops.object.editmode_toggle()
bpy.ops.uv.select_all(action='SELECT')

bpy.ops.uv.zenuv_set_texel_density('INVOKE_DEFAULT')

bpy.ops.object.editmode_toggle()

bpy.context.object.data.uv_layers["uv_maps"].active_render = True
bpy.context.object.data.uv_layers['uv_fabrics'].active = True
