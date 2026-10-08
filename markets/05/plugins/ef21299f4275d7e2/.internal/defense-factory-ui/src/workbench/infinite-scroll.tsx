import { LoadingIndicator } from "@oai/ds/ui/indicator";
import { useCallback, useLayoutEffect, useRef } from "react";

export function InfiniteScroll({
  enabled,
  loading,
  onLoadMore,
}: {
  enabled: boolean;
  loading: boolean;
  onLoadMore: () => void;
}) {
  const onLoadMoreRef = useRef(onLoadMore);
  useLayoutEffect(() => {
    onLoadMoreRef.current = onLoadMore;
  }, [onLoadMore]);

  const observe = useCallback(
    (element: HTMLDivElement | null) => {
      if (!element || !enabled || loading) return;
      let active = true;
      const observer = new IntersectionObserver(([entry]) => {
        if (!active || !entry.isIntersecting) return;
        active = false;
        observer.disconnect();
        onLoadMoreRef.current();
      });
      observer.observe(element);
      return () => {
        active = false;
        observer.disconnect();
      };
    },
    [enabled, loading],
  );

  return (
    <div ref={observe} className="flex h-6 w-6 items-center justify-center">
      {loading && <LoadingIndicator className="h-4 w-4" />}
    </div>
  );
}
