# inside src/icons/ folder, there are css files like the following:

# /* A-Frame -> aframe.svg */
# article a[href*='aframe.io']::before {
#   -webkit-mask-image: url("data:image/svg+xml,%3csvg role='img' viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'%3e%3ctitle%3eA-Frame%3c/title%3e%3cpath d='M17.37 17.07H6.57L4.24 24H3.01l8.23-24h1.52l8.23 24h-1.3zm-.39-1.13l-5-14.96-5.03 14.98h10.03Z'/%3e%3c/svg%3e");
#   mask-image: url("data:image/svg+xml,%3csvg role='img' viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'%3e%3ctitle%3eA-Frame%3c/title%3e%3cpath d='M17.37 17.07H6.57L4.24 24H3.01l8.23-24h1.52l8.23 24h-1.3zm-.39-1.13l-5-14.96-5.03 14.98h10.03Z'/%3e%3c/svg%3e");
# }

# This script will convert the svg data to a file and replace the data with the file path
# /* A-Frame -> aframe.svg */
# article a[href*='aframe.io']::before {
#   -webkit-mask-image: url("https://simpleicons.org/icons/aframe.svg");
#   mask-image: url("https://simpleicons.org/icons/aframe.svg");
# }

import os

url = "https://simpleicons.org/icons/"

# for all files in /src/icons
for file in os.listdir("src/icons"):
    if file.endswith(".css"):
        # read the file
        with open(os.path.join("src/icons", file), "r") as f:
            data = f.read()
            # while the file includes any "data:image/svg+xml" string
            while "data:image/svg+xml" in data:
                # get the index of the string
                index = data.index("data:image/svg+xml")
                # svg%3e");
                end = data.index(");", index)
                # get the svg data
                svg = data[index:end]
                # get the by finding the closest comment
                comment = data[:index]
                comment = comment[comment.rindex("/*") :]
                comment = comment[comment.index("->") + 2 :]
                comment = comment[: comment.index(".svg")]
                comment.strip()
                # replace the data with the file path
                data = data.replace(svg, url + comment + ".svg")
        # write the file
        with open(os.path.join("src", file), "w") as f:
            f.write(data)
