bl_info = {
    'name' : 'Hoe Doen Ze Het',
    'author' : 'Hans Willem Gijzel',
    'version' : (1, 0),
    'blender' : (2, 79),
    'location' : 'View 3D > Tools > Hoe Doen Ze Het',
    'description' : 'Duplicates selected object and moves it to the 3d curslor location',
    'warning' : '',
    'wiki_url' : '',
    'category' : 'Hoe Doen Ze Het'
    }


import bpy


def main_dupMove():
    cursor_pos = bpy.context.scene.cursor_location
    obj = bpy.context.active_object
    new_obj = obj.copy()
    new_obj.location = cursor_pos
    bpy.context.scene.objects.link(new_obj)


#panel
class Panel_dupMove(bpy.types.Panel):
    
    #panel attributes
    '''Duplicate And Move.'''
    bl_label = 'Duplicate And Move'
    bl_idname = 'tools_hoe_doen_ze_het_duplicate_and_move'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Hoe Doen Ze Het'
    
    #draw loop
    def draw(self, context):
        layout = self.layout
        col = layout.column(align = True)
        col.operator('script.operator_dup_move', text = 'Duplicate And Move')


#operator
class Operator_dupMove(bpy.types.Operator):
    
    #operator attributes
    '''Duplicates selected object and moves it to the 3d curslor location'''
    bl_label = 'Operator Duplicate And Move'
    bl_idname = 'script.operator_dup_move'
    bl_options = {'REGISTER', 'UNDO'}

    #execute
    def execute(self, context):
        main_dupMove()
        
        return {'FINISHED'}


#register / unregister
def register():
    bpy.utils.register_class(Operator_dupMove)
    bpy.utils.register_class(Panel_dupMove)

    
def unregister():
    bpy.utils.unregister_class(Operator_dupMove)
    bpy.utils.register_class(Panel_dupMove)


#enable to test the addon by running this script
if __name__ == '__main__':
    register()
