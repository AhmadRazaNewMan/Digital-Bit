/** Canonical track order — keep aligned with `MODULES` in `scripts/daily_post.py`. */
export type ModuleMeta = {
  id: string;
  label: string;
  tagline: string;
  /** CSS hue for accents */
  hue: number;
};

export const MODULE_CATALOG: ModuleMeta[] = [
  {
    id: "dsa-algorithms",
    label: "DSA & algorithms",
    tagline: "Complexity, patterns, interview readiness",
    hue: 271,
  },
  {
    id: "frontend-basics",
    label: "Frontend foundations",
    tagline: "UI structure, accessibility, and rendering speed",
    hue: 319,
  },
  {
    id: "javascript-typescript",
    label: "JavaScript & TypeScript",
    tagline: "Type-safe apps, async control, cleaner abstractions",
    hue: 47,
  },
  {
    id: "backend",
    label: "Backend",
    tagline: "Production-grade endpoints and failure handling",
    hue: 66,
  },
  {
    id: "system-design",
    label: "System design",
    tagline: "Scale, tradeoffs, and architecture judgement",
    hue: 95,
  },
  {
    id: "devops",
    label: "DevOps",
    tagline: "Build, release, observe, and recover confidently",
    hue: 223,
  },
  {
    id: "dbms",
    label: "Databases",
    tagline: "Storage design and performance tuning fundamentals",
    hue: 175,
  },
];

export const MODULE_IDS = MODULE_CATALOG.map((m) => m.id);

export function moduleMeta(id: string): ModuleMeta | undefined {
  return MODULE_CATALOG.find((m) => m.id === id);
}
