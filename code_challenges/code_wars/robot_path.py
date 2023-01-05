class RobotDirections:
    def __init__(self, directions):
        self.directions = directions

    def translate_directions(self):
        translated_instructions = []
        direction_translation = {
            "<": "left",
            ">": "right",
            "^": "up",
            "v": "down",
        }
        i = 0
        j = i + 1
        if self.directions == "":
            return "Paused"

        for _ in range(len(self.directions) + 1):
            if j == len(self.directions):
                if len(self.directions[i:j]) == 1:
                    translated_instructions.append(
                        f"Take 1 step {direction_translation[self.directions[i]]}"
                    )
                    return "\n".join(translated_instructions)
                else:
                    translated_instructions.append(
                        f"Take {len(self.directions[i:j])} steps {direction_translation[self.directions[i]]}"
                    )
                    return "\n".join(translated_instructions)
            while self.directions[i] == self.directions[j]:
                j += 1
                if j == len(self.directions):
                    break
            if len(self.directions[i:j]) == 1:
                translated_instructions.append(
                    f"Take 1 step {direction_translation[self.directions[i]]}"
                )
                if j == len(self.directions):
                    break
                i = j
                j = i + 1
            else:
                translated_instructions.append(
                    f"Take {len(self.directions[i:j])} steps {direction_translation[self.directions[i]]}"
                )
                if j == len(self.directions):
                    break
                i = j
                j = i + 1
        return "\n".join(translated_instructions)


def walk(directions):
    instructions = RobotDirections(directions)

    return instructions.translate_directions()


if __name__ == "__main__":
    directions = ">>"
    print(walk(directions))
