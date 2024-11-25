"use client";
import { Carousel } from "flowbite-react";

const customTheme = {
  root: {
    base: "relative h-full w-full",
    leftControl:
      "absolute left-0 top-0 flex h-full items-center justify-center px-4 focus:outline-none",
    rightControl:
      "absolute right-0 top-0 flex h-full items-center justify-center px-4 focus:outline-none",
  },
  indicators: {
    active: {
      off: "hidden",
      on: "hidden",
    },
    base: "hidden",
    wrapper: "hidden",
  },
  item: {
    base: "absolute left-1/2 top-1/2 block w-full -translate-x-1/2 -translate-y-1/2",
    wrapper: {
      off: "w-full flex-shrink-0 transform cursor-default snap-center",
      on: "w-full flex-shrink-0 transform cursor-grab snap-center",
    },
  },
  control: {
    base: "inline-flex h-8 w-8 items-center justify-center rounded-full bg-black/30 group-hover:bg-black/50 group-focus:outline-none group-focus:ring-4 group-focus:ring-black dark:bg-gray-800/30 dark:group-hover:bg-gray-800/60 dark:group-focus:ring-gray-800/70 sm:h-10 sm:w-10",
    icon: "h-5 w-5 text-black dark:text-gray-800 sm:h-6 sm:w-6",
  },
  scrollContainer: {
    base: "flex h-full snap-mandatory overflow-y-hidden overflow-x-scroll scroll-smooth rounded-lg",
    snap: "snap-x",
  },
};

export function ChartCarousel({ iframeSrcs }) {
  const iframeStyle = { border: "none", height: "100%", width: "100%" };

  return (
    <div className="h-96 sm:h-128 xl:h-160 2xl:h-192">
      <Carousel slide={false} theme={customTheme}>
        {iframeSrcs.map((src, index) => (
          <iframe key={index} src={src} style={iframeStyle} title={`iframe-${index}`}></iframe>
        ))}
      </Carousel>
    </div>
  );
}

export default ChartCarousel;
