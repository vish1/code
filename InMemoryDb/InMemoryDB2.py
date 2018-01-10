

class InMemoryDB():
    def __init__(self):
        self.db = {}
        self.rollback_logs = []
        self.counts = {}
        self.in_block = False

    def set(self, key, value):
        old_value = self.db.get(key, None)
        self.db[key] = value
        if old_value:
            self.counts[old_value] = self.counts[old_value] - 1
        self.counts[value] = self.counts.get(value, 0) + 1

    def get(self, key):
        return self.db.get(key, None)

    def delete(self, key):
        if key in self.db.keys():
            old_value = self.db.get(key, 0)
            self.counts[old_value] = self.counts[old_value] - 1
            del self.db[key]

    def count(self, value):
        print self.counts.get(value, 0)

    def process_input(self, inp):
        inp = inp.split(' ')
        if len(inp) == 3:
            if inp[0].upper() == "SET":
                if self.in_block:
                    if inp[1]:
                        command = "SET "+str(inp[1])+" "+ str(self.get(inp[1]))
                    else:
                        command = "DELETE "+str(inp[1])
                    self.rollback_logs[len(self.rollback_logs)-1].append(command)
                self.set(inp[1], inp[2])
                return
        elif len(inp) == 2:
            if inp[0].upper() == 'GET':
                r_value = self.get(inp[1])
                if r_value:
                    print r_value
                else:
                    print "NULL"
                return
            elif inp[0].upper() == 'DELETE':
                if self.in_block:
                    if inp[1]:
                        command = "SET "+str(inp[1])+" "+str(self.get(inp[1]))
                        self.rollback_logs[len(self.rollback_logs)-1].append(command)
                self.delete(inp[1])
                return
            elif inp[0].upper() == "COUNT":
                self.count(inp[1])
                return
        elif len(inp) == 1:
            if inp[0].upper() == "END":
                exit(0)
            elif inp[0].upper() == "BEGIN":
                self.in_block = True
                self.rollback_logs.insert(len(self.rollback_logs), [])
                return
            elif inp[0].upper() == "COMMIT":
                self.in_block = False
                self.rollback_logs = []
                return
            elif inp[0].upper() == "ROLLBACK":
                if len(self.rollback_logs) == 0:
                    print "NO TRANSACTION"
                    return
                self.in_block = False
                rollback = self.rollback_logs[len(self.rollback_logs) - 1]
                del self.rollback_logs[len(self.rollback_logs) - 1]
                for command in reversed(rollback):
                    self.process_input(command)


if __name__ == "__main__":
    print "This is an in-memory DB"
    db = InMemoryDB()
    while True:
        inp = raw_input(">>> ").strip()
        db.process_input(inp)
