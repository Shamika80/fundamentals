import DrawIO

# Create a new DrawIO object
diagram = DrawIO()

# Add shapes (tables)
books_table = diagram.add_table('Books', columns=['book_id (PK)', 'title', '...'])
authors_table = diagram.add_table('Authors', columns=['author_id (PK)', 'first_name', '...'])

# Add relationships
diagram.add_relationship(books_table, authors_table, label='one-to-many')

# Save the diagram
diagram.save('bookhaven_erd.drawio')