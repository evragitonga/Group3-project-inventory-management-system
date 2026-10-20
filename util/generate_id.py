def generate_id(cls, initials, dictionary):
  while True:
      cls._next_id += 1
      generated_id = f"{initials}{cls._next_id}"

      if generated_id not in dictionary:
          return generated_id
