# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: PetCare
class TagManager:
    def __init__(self, db):
        self.db = db
    
    def add_tag(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0: return False
        existing = [t for t in self.db.tags.values() if t['name'].strip().lower() == name.strip().lower()]
        if existing: return True
        new_id = max(self.db.tags.keys(), default=0) + 1
        self.db.tags[new_id] = {'id': new_id, 'name': name.strip()}
        for pet in self.db.pets.values():
            if not isinstance(pet.get('tags'), list): pet['tags'] = []
            if new_id not in pet['tags']: pet['tags'].append(new_id)
        return True
    
    def remove_tag(self, tag_name):
        target_ids = [t['id'] for t in self.db.tags.values() if t['name'].strip().lower() == tag_name.strip().lower()]
        if not target_ids: return False
        for pet in self.db.pets.values():
            if isinstance(pet.get('tags'), list):
                pet['tags'] = [tid for tid in pet['tags'] if tid not in target_ids]
        del_tag_count = sum(1 for t in self.db.tags.values() if t['id'] in target_ids)
        if del_tag_count == 0: return False
        for k, v in list(self.db.tags.items()):
            if v['id'] in target_ids: del self.db.tags[k]
        return True
