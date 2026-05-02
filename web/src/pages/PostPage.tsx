import { Link, Navigate, useParams } from "react-router-dom";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { DigitalBackground } from "../components/DigitalBackground";
import { getPost } from "../lib/posts";

export function PostPage() {
  const { moduleId = "", postId = "" } = useParams();
  const mod = decodeURIComponent(moduleId);
  const pid = decodeURIComponent(postId);
  const post = getPost(mod, pid);

  if (!post) {
    return <Navigate to="/" replace />;
  }

  return (
    <article className="post">
      <DigitalBackground />
      <div className="post__inner">
        <Link to="/" className="backlink">
          ← All modules
        </Link>
        <p className="post__module">{post.moduleId.replace(/-/g, " ")}</p>
        <h1 className="post__title">{post.title}</h1>
        <div className="post__body markdown-body">
          <ReactMarkdown remarkPlugins={[remarkGfm]}>{post.body}</ReactMarkdown>
        </div>
      </div>
    </article>
  );
}
