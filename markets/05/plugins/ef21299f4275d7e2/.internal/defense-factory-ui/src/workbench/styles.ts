// Keep the operations workspace visually consistent without changing the
// presentation of older Aardvark or shared/core surfaces.
export const workbenchStyles = {
  collectionPage: "df-collection-page",
  detailPage: "flex w-full flex-col gap-8 pb-12",
  scanDetailPage:
    "flex min-h-0 w-full flex-1 flex-col gap-8 overflow-hidden [&>header]:shrink-0",
  outputsGrid:
    "grid h-full min-h-0 min-w-0 grid-rows-[minmax(0,8rem)_minmax(0,1fr)] overflow-hidden sm:grid-cols-[minmax(10rem,15rem)_minmax(0,1fr)] sm:grid-rows-[minmax(0,1fr)]",
  outputsSidebar:
    "border-token-border-light bg-token-bg-primary min-h-0 overflow-y-auto overscroll-contain border-b p-2 sm:border-e sm:border-b-0 dark:bg-token-bg-secondary-surface",
  outputsPreview:
    "bg-token-bg-secondary-surface min-h-0 min-w-0 overflow-auto overscroll-contain p-6 dark:bg-token-bg-primary",
  collectionTitle:
    "text-token-text-primary min-w-0 max-w-full text-xl font-semibold tracking-tight break-words",
  detailTitle:
    "text-token-text-primary min-w-0 max-w-full text-2xl font-semibold tracking-tight break-words",
  sectionTitle: "text-token-text-primary text-base font-medium",
  description: "text-token-text-secondary text-[14px] leading-5",
  card: "border-token-border-light bg-token-bg-primary rounded-2xl border",
  table: "df-collection-table",
  tableRow: "h-[60px]",
  control: "df-control max-w-full",
  selectControl:
    "df-control interactive-button-secondary interactive-outline-secondary border-token-border-medium bg-token-bg-primary min-w-0 max-w-full gap-2 px-3 [&>span:first-child]:truncate [&>span:last-child]:shrink-0",
  link: "text-token-text-accent underline-offset-2 hover:underline",
  tableLink: "text-token-text-primary underline-offset-2 hover:underline",
  tableSecondaryValue: "text-token-text-secondary whitespace-nowrap",
  tableIdentifierValue:
    "text-token-text-secondary font-mono text-[12px] tracking-tight",
  metadataLabel: "text-token-text-secondary text-[12px] leading-4",
  metadataValue: "text-token-text-primary text-[14px] leading-5",
  metadataGrid: "grid gap-x-8 gap-y-5 sm:grid-cols-2",
};
