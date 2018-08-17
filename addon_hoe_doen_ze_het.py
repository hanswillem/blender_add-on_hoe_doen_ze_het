bl_info = {
    'name' : 'Hoe Doen Ze Het',
    'author' : 'Hans Willem Gijzel',
    'version' : (1, 0),
    'blender' : (2, 79),
    'location' : 'View 3D > Tools > Hoe Doen Ze Het',
    'description' : 'Some functions for the HOE DOEN ZE HET? project',
    'warning' : '',
    'wiki_url' : '',
    'category' : 'Hoe Doen Ze Het'
    }


import bpy

#duplicate and move the selected objects
def main_dupMove():
    cursor_pos = bpy.context.scene.cursor_location
    obj = bpy.context.active_object
    new_obj = obj.copy()
    new_obj.location = cursor_pos
    bpy.context.scene.objects.link(new_obj)


#hide all bones that have no custom shape
def main_hideBones():
    obs = bpy.data.objects
    for i in obs:
        if i.type == 'ARMATURE':
            for j in i.pose.bones:
                if j.custom_shape == None:
                    j.bone.hide = True


#unhide all bones
def main_unhideBones():
    obs = bpy.data.objects
    for i in obs:
        if i.type == 'ARMATURE':
            for j in i.data.bones:
                j.hide = False 


#freeze transformation of selected object
def main_freeze():
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bpy.ops.object.transforms_to_deltas(mode='LOC')


#unfreeze transformation of selected object
def main_resetPSR():
    bpy.ops.object.rotation_clear(clear_delta=False)
    bpy.ops.object.scale_clear(clear_delta=False)
    bpy.ops.object.location_clear(clear_delta=False)


#panel
class Panel_hoeDoenZeHet(bpy.types.Panel):
    
    #panel attributes
    '''Duplicate And Move.'''
    bl_label = 'Hoe doen ze het'
    bl_idname = 'tools_hoe_doen_ze_het'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Hoe Doen Ze Het'
    
    #draw loop
    def draw(self, context):
        layout = self.layout
        col = layout.column(align = True)
        col.operator('script.operator_dup_move', text = 'Duplicate And Move')
        col.operator('script.operator_freeze', text = 'Freeze Transforms')
        col.operator('script.operator_reset_psr', text = 'Reset Transforms')
        col.operator('script.operator_hide_bones', text = 'Hide Bones')
        col.operator('script.operator_unhide_bones', text = 'Unhide Bones')


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



#operator
class Operator_freeze(bpy.types.Operator):
    
    #operator attributes
    '''Freezes the transforms of the selected object'''
    bl_label = 'Operator Freeze Transforms'
    bl_idname = 'script.operator_freeze'
    bl_options = {'REGISTER', 'UNDO'}

    #execute
    def execute(self, context):
        main_freeze()
        
        return {'FINISHED'}


#operator
class Operator_resetPSR(bpy.types.Operator):
    
    #operator attributes
    '''Resets the transforms of the selected object'''
    bl_label = 'Operator Reset PSR'
    bl_idname = 'script.operator_reset_psr'
    bl_options = {'REGISTER', 'UNDO'}

    #execute
    def execute(self, context):
        main_resetPSR()
        
        return {'FINISHED'}


#operator
class Operator_hideBones(bpy.types.Operator):
    
    #operator attributes
    '''Hides bones without custom shape'''
    bl_label = 'Operator Hide Bones'
    bl_idname = 'script.operator_hide_bones'
    bl_options = {'REGISTER', 'UNDO'}

    #execute
    def execute(self, context):
        main_hideBones()
        
        return {'FINISHED'}


#operator
class Operator_unhideBones(bpy.types.Operator):
    
    #operator attributes
    '''Unhides bones without custom shape'''
    bl_label = 'Operator Unhide Bones'
    bl_idname = 'script.operator_unhide_bones'
    bl_options = {'REGISTER', 'UNDO'}

    #execute
    def execute(self, context):
        main_unhideBones()
        
        return {'FINISHED'}



#register / unregister
def register():
    bpy.utils.register_class(Panel_hoeDoenZeHet)
    bpy.utils.register_class(Operator_dupMove)
    bpy.utils.register_class(Operator_freeze)
    bpy.utils.register_class(Operator_resetPSR)
    bpy.utils.register_class(Operator_hideBones)
    bpy.utils.register_class(Operator_unhideBones)


def unregister():
    bpy.utils.unregister_class(Panel_hoeDoenZeHet)
    bpy.utils.unregister_class(Operator_dupMove)
    bpy.utils.unregister_class(Operator_freeze)
    bpy.utils.unregister_class(Operator_resetPSR)
    bpy.utils.unregister_class(Operator_hideBones)
    bpy.utils.unregister_class(Operator_unhideBones)



#enable to test the addon by running this script
if __name__ == '__main__':
    register()
