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
      off: "bg-white/50 hover:bg-white dark:bg-gray-800/50 dark:hover:bg-gray-800",
      on: "bg-white dark:bg-gray-800",
    },
    base: "h-3 w-3 rounded-full",
    wrapper: "absolute bottom-5 left-1/2 flex -translate-x-1/2 space-x-3",
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

export function Component(props) {
  return (
    <div className="h-56 sm:h-64 xl:h-80 2xl:h-96">
      <Carousel slide={false} theme={customTheme}>
        <iframe
          src="http://localhost:8050/tractos_age"
          style={{ border: "none", height: "100%", width: "100%" }}
        ></iframe>
        <iframe
          src="http://localhost:8050/tractos_repair_distribution"
          style={{ border: "none", height: "100%", width: "100%" }}
        ></iframe>
        <iframe
          src="http://localhost:8050/tractos_age"
          style={{ border: "none", height: "100%", width: "100%" }}
        ></iframe>
        <img
          src="https://flowbite.com/docs/images/carousel/carousel-5.svg"
          alt="..."
        />
      </Carousel>
    </div>
  );
}

export default Component;
