from dataclasses import dataclass

@dataclass
class Node:
    user_id: str
    short_name: str
    long_name: str

    @property
    def short_padded(self, pad_to: int = 4) -> str:
        """
        short_name padded to four characters.
        Emoji are two characters wide, which throws off Python's normal padding.
        """
        if (len(self.short_name) == 1): pad_to -= 1
        return self.short_name.ljust(pad_to)
    
    @property
    def node_list_disp(self):
        return f"{self.user_id} {self.short_padded} | {self.long_name}"
    
