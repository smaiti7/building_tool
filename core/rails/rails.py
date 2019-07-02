import bmesh

from .rails_types import create_railing_from_selection
from ...utils import get_edit_mesh


class Rails:
    @classmethod
    def build(cls, context, props):
        me = get_edit_mesh()
        bm = bmesh.from_edit_mesh(me)

        if cls.validate(bm):
            create_railing_from_selection(bm, props)
            bmesh.update_edit_mesh(me, True)
            return {"FINISHED"}
        return {"CANCELLED"}

    @classmethod
    def validate(cls, bm):
        """ Ensure valid user selection if any """
        faces = [f for f in bm.faces if f.select]
        if faces:
            if all([f.normal.z for f in faces]):
                return True

        edges = [e for e in bm.edges if e.select]
        if edges and not faces:
            return True

        return False
