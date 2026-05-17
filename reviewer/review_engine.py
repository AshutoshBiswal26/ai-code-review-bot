class ReviewEngine:

    def review_files(self, files):

        for file in files:

            print("\n" + "=" * 60)

            print(f"File: {file['filename']}")
            print(f"Additions: {file['additions']}")
            print(f"Deletions: {file['deletions']}")

            print("\nPatch:\n")
            print(file["patch"])

            print("=" * 60 + "\n")