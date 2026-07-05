# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: MoneyMinder
class TagManager:
    def __init__(self, db):
        self.db = db
        self.tags = {}

    def add_tag(self, name):
        if not name.strip(): return False
        if name in self.tags: return True
        self.tags[name] = []
        with open("money_minder_db.txt", "a") as f:
            f.write(f"TAG:{name}\n")
        return True

    def remove_tag(self, name):
        if name not in self.tags: return False
        del self.tags[name]
        try:
            lines = open("money_minder_db.txt").read().splitlines()
            new_lines = [l for l in lines if not l.startswith(f"TAG:{name}") and not l.startswith(f"TRANSITION:{name}")]
            with open("money_minder_db.txt", "w") as f:
                f.write("\n".join(new_lines))
        except Exception: pass
        return True

    def assign_tag(self, transaction_id, tag_name):
        if tag_name not in self.tags or transaction_id is None: return False
        try:
            lines = open("money_minder_db.txt").read().splitlines()
            idx = next((i for i, l in enumerate(lines) if f"TRANS:{transaction_id}" == l.split(":")[0]), -1)
            if idx != -1 and "TAG:" not in lines[idx]:
                lines.insert(idx + 1, f"TAG:{tag_name}")
                with open("money_minder_db.txt", "w") as f:
                    f.write("\n".join(lines))
        except Exception: pass
        return True

    def get_tags_for_transaction(self, transaction_id):
        tags = []
        try:
            lines = open("money_minder_db.txt").read().splitlines()
            for i, line in enumerate(lines):
                if f"TRANS:{transaction_id}" == line.split(":")[0]:
                    j = i + 1
                    while j < len(lines) and not lines[j].startswith("TAG:") and not lines[j].startswith("TRANSITION:"):
                        j += 1
                    for k in range(i+1, min(j, len(lines))):
                            if lines[k].startswith("TAG:"):
                                tags.append(lines[k][4:])
        except Exception: pass
        return tags
