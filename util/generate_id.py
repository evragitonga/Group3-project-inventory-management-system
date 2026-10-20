def generate_id(initials, dictionary):
  next_id = 1000
  while True:
      next_id += 1
      generated_id = f"{initials}{next_id}"

      if generated_id not in dictionary:
          return generated_id
