const FAQcontent = () => {
  return (
    <section className="dark:bg-gray-100 dark:text-gray-800">
      <div className="container flex flex-col justify-center px-4 py-8 mx-auto md:p-8">
        <h2 className="text-2xl font-semibold sm:text-4xl">
          Frequently Asked Questions
        </h2>
        <p className="mt-4 mb-8 dark:text-gray-600">
          These are a few common questions asked about our application
        </p>
        <div className="space-y-4">
          <details className="w-full border rounded-lg">
            <summary className="px-4 py-6 focus:outline-none focus-visible:dark:ring-violet-600">
              How are the users talking to each other in real-time?
            </summary>
            <p className="px-4 py-6 pt-0 ml-4 -mt-4 dark:text-gray-600">
              By using Socket.IO. Socket.IO is an event-driven library for
              real-time web applications. It enables real-time, bi-directional
              communication between web clients and servers. It consists of two
              components: a client, and a server. Both components have nearly
              identical API.
            </p>
          </details>
          <details className="w-full border rounded-lg">
            <summary className="px-4 py-6 focus:outline-none focus-visible:dark:ring-violet-600">
              Why did you even create this app?
            </summary>
            <p className="px-4 py-6 pt-0 ml-4 -mt-4 dark:text-gray-600">
              Because it was a fun way to explore new technologies.
            </p>
          </details>
          <details className="w-full border rounded-lg">
            <summary className="px-4 py-6 focus:outline-none focus-visible:dark:ring-violet-600">
              What methodologies did you use?
            </summary>
            <p className="px-4 py-6 pt-0 ml-4 -mt-4 dark:text-gray-600">
              We used Agile methodology for this project.
            </p>
          </details>
        </div>
      </div>
    </section>
  );
};

export default FAQcontent;
