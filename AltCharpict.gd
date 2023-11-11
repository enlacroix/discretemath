extends TextureRect

@onready var extra_texture


'''
_get_drop_data
_can_drop_data
_drop_data
'''
func _ready():
	extra_texture = texture
	
func _get_drag_data(at_position):
	var preview_texture = TextureRect.new()
	preview_texture.texture = texture
	preview_texture.expand_mode = 1
	preview_texture.size = Vector2(70, 85)
	
	var frame = Sprite2D.new()
	frame.texture = load("res://src/assets/interface/BLUEFRAME.png")
	frame.scale = Vector2(0.555, 0.555)
	frame.position = Vector2(35, 42)
	
	var preview = Control.new()
	preview.add_child(preview_texture)
	preview.add_child(frame)
	set_drag_preview(preview)
	
	texture = null
 
	return preview_texture.texture
 
 
func _can_drop_data(_pos, data):
	return data is Texture2D and texture == null
 
 
func _drop_data(_pos, data):
	texture = data

func _notification(what):
	if what == NOTIFICATION_DRAG_END:
		if is_drag_successful():
			extra_texture = texture
		else:
			texture = extra_texture
	

