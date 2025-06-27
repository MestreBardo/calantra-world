import os
import re

vault_path = "./content/Lugares"  # ← Substitua por seu caminho local
index_path = os.path.join("./content", "Indice de Locais.md")

categorias = {
    "ruina": "🧱 Ruínas",
    "fortaleza": "🏰 Fortalezas",
    "vila": "🏘️ Vilas",
    "cidade": "🏙️ Cidades",
    "regiao": "🗺️ Regiões",
    "reino": "👑 Reinos",
    "continente": "🌍 Continentes"
}

locais = {k: [] for k in categorias}

for root, _, files in os.walk(vault_path):
    for filename in files:
        if not filename.endswith(".md") or filename == "Indice de Locais.md":
            continue

        path = os.path.join(root, filename)
        with open(path, encoding="utf-8") as file:
            content = file.read()

            # Extrair frontmatter YAML se presente
            match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            frontmatter = match.group(1) if match else ""
            inTagSection = False
            tags = []
            draft = False

            # Verifica se há tags e draft no frontmatter
            for line in frontmatter.splitlines():
                if line.strip().startswith("tags:"):
                    inTagSection = True
                    continue
                elif line.strip().startswith("draft:"):
                    draft = "true" in line.lower()
                    inTagSection = False
                elif inTagSection:
                    tag = [t.strip() for t in re.findall(r"[-\s]*([^\[\],]+)", line) if t.strip()]
                    tags.extend(tag)
                    print(f"Tags encontradas: {tags}")

            # Ignorar se for draft ou modelo
            if draft or any("modelo" in t.lower() for t in tags):
                continue

            # Categorizar por tipo/xxxxx
            for tipo, titulo in categorias.items():
                if f"tipo/{tipo}" in tags:
                    locais[tipo].append(filename.replace(".md", ""))
                    break

# Gerar Indice
with open(index_path, "w", encoding="utf-8") as index:
    index.write("---\n\n")
    index.write("title: Índice de Locais\n")
    index.write("tags:\n")
    index.write("  - mundo\n")
    index.write("  - índice\n")
    index.write("  - geografia\n")
    index.write("created: 2025-06-27\n")
    index.write("---\n\n")
    index.write("> [!abstract] Este documento organiza todos os lugares de calantra em ordem hierárquica: de ruínas e vilas até continentes e o plano mundial. Cada localidade pode ter uma ou mais subentidades ligadas a ela.\n\n")
    index.write("---\n\n")

    for tipo, titulo in categorias.items():
        index.write(f"> [!note]- {titulo}\n>\n")
        for nome in sorted(locais[tipo]):
            index.write(f"> - [[{nome}]]\n")
        index.write("\n")
        index.write("---\n\n")

    index.write("*Gerado automaticamente.*\n")
