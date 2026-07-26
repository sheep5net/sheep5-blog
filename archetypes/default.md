+++
date = '{{ .Date }}'
draft = true
title = '{{ replace .File.ContentBaseName "-" " " | title }}'
slug = '{{ math.Rand | mul 89999 | add 10000 | math.Floor | printf "%05.0f" }}'
images = ['og-image.jpg']
+++
