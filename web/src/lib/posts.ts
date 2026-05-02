import { MODULE_CATALOG, type ModuleMeta } from "./moduleCatalog";

export type Post = {
  moduleId: string;
  postId: string;
  title: string;
  body: string;
  sourceKey: string;
};

function extractTitle(md: string): string {
  for (const line of md.split(/\r?\n/)) {
    const t = line.trim();
    if (t.startsWith("# ")) return t.slice(2).trim();
    if (t.startsWith("#\t")) return t.slice(2).trim();
  }
  return "Untitled";
}

function parsePathKey(key: string): { moduleId: string; postId: string } | null {
  const norm = key.replace(/\\/g, "/");
  const m = norm.match(/content\/modules\/([^/]+)\/([^/]+)\.md$/i);
  if (!m) return null;
  const postId = m[2];
  return { moduleId: m[1], postId };
}

const rawModules = import.meta.glob("../../../content/modules/**/*.md", {
  eager: true,
  query: "?raw",
  import: "default",
}) as Record<string, string>;

export function getAllPosts(): Post[] {
  const posts: Post[] = [];
  for (const [key, body] of Object.entries(rawModules)) {
    const parsed = parsePathKey(key);
    if (!parsed) continue;
    posts.push({
      moduleId: parsed.moduleId,
      postId: parsed.postId,
      title: extractTitle(body),
      body,
      sourceKey: key,
    });
  }
  posts.sort((a, b) => b.postId.localeCompare(a.postId));
  return posts;
}

export function getPost(moduleId: string, postId: string): Post | undefined {
  return getAllPosts().find((p) => p.moduleId === moduleId && p.postId === postId);
}

export type ModuleSummary = ModuleMeta & { count: number };

/** Ordered tracks from catalog (including 0-note tracks), then any stray folders from disk. */
export function getModules(): ModuleSummary[] {
  const posts = getAllPosts();
  const counts = new Map<string, number>();
  for (const p of posts) {
    counts.set(p.moduleId, (counts.get(p.moduleId) ?? 0) + 1);
  }

  const known = new Set(MODULE_CATALOG.map((m) => m.id));
  const ordered: ModuleSummary[] = MODULE_CATALOG.map((m) => ({
    ...m,
    count: counts.get(m.id) ?? 0,
  }));

  const extras = [...counts.entries()]
    .filter(([id]) => !known.has(id))
    .sort(([a], [b]) => a.localeCompare(b))
    .map(([id, count]) => ({
      id,
      label: id.replace(/-/g, " ").replace(/\b\w/g, (c) => c.toUpperCase()),
      tagline: "Community notes",
      hue: (id.length * 61) % 360,
      count,
    }));

  return [...ordered, ...extras];
}
