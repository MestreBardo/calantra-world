import os
import re

vault_path = "/content"  # ← Substitua por seu caminho local
index_path = os.path.join(vault_path, "Indice de Locais.md")

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

            tags = []
            draft = False

            # Verifica se há tags e draft no frontmatter
            for line in frontmatter.splitlines():
                if line.strip().startswith("tags:"):
                    tags = re.findall(r"[-\s]*([^\[\],]+)", line)
                    tags = [t.strip() for t in tags if t.strip()]
                elif line.strip().startswith("draft:"):
                    draft = "true" in line.lower()

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
    index.write("# 🌐 Indice de Locais\n\n")
    index.write("> [!abstract] Lista atualizada automaticamente com locais oficiais e finalizados.\n\n")

    for tipo, titulo in categorias.items():
        index.write(f"> [!note]- {titulo}\n>\n")
        for nome in sorted(locais[tipo]):
            index.write(f"> - [[{nome}]]\n")
        index.write("\n")

    index.write("*Gerado automaticamente.*\n")
