const IndividualMember = () => {
  return (
    <article className="max-w-2xl px-6 py-24 mx-auto space-y-12 dark:bg-gray-100 dark:text-gray-900">
      <div className="w-full mx-auto space-y-4 text-center">
        <p className="text-xs font-semibold tracking-wider uppercase">
          #welovecoding
        </p>
        <h1 className="text-4xl font-bold leading-tight md:text-5xl">
          Want to know more about the members?
        </h1>
      </div>

      <div className="pt-12 border-t dark:border-gray-300">
        <div className="flex flex-col space-y-4 md:space-y-0 md:space-x-6 md:flex-row">
          <img
            src="https://i.ibb.co/JdXWqkm/maisha.jpg"
            alt=""
            className="self-center flex-shrink-0 w-24 h-24 border rounded-full md:justify-self-start dark:bg-gray-500 dark:border-gray-300"
          />
          <div className="flex flex-col">
            <h4 className="text-lg font-semibold">Maisha Zaman</h4>
            <p className="dark:text-gray-600">The elite backend developer.</p>
          </div>
        </div>
      </div>
      <div className="pt-12 border-t dark:border-gray-300">
        <div className="flex flex-col space-y-4 md:space-y-0 md:space-x-6 md:flex-row">
          <img
            src="https://i.ibb.co/Kjgjx2p/mohona.jpg"
            alt=""
            className="self-center flex-shrink-0 w-24 h-24 border rounded-full md:justify-self-start dark:bg-gray-500 dark:border-gray-300"
          />
          <div className="flex flex-col">
            <h4 className="text-lg font-semibold">Mahfuja Akter Mohona</h4>
            <p className="dark:text-gray-600">The UI/UX designer.</p>
          </div>
        </div>
      </div>
      <div className="pt-12 border-t dark:border-gray-300">
        <div className="flex flex-col space-y-4 md:space-y-0 md:space-x-6 md:flex-row">
          <img
            src="https://i.ibb.co/7V3gWCw/oishi.jpg"
            alt=""
            className="self-center flex-shrink-0 w-24 h-24 border rounded-full md:justify-self-start dark:bg-gray-500 dark:border-gray-300"
          />
          <div className="flex flex-col">
            <h4 className="text-lg font-semibold">Samia Alam Oishi</h4>
            <p className="dark:text-gray-600">The Frontend Developer.</p>
          </div>
        </div>
      </div>
      <div className="pt-12 border-t dark:border-gray-300">
        <div className="flex flex-col space-y-4 md:space-y-0 md:space-x-6 md:flex-row">
          <img
            src="https://i.ibb.co/Bt3JrCv/riya.jpg"
            alt=""
            className="self-center flex-shrink-0 w-24 h-24 border rounded-full md:justify-self-start dark:bg-gray-500 dark:border-gray-300"
          />
          <div className="flex flex-col">
            <h4 className="text-lg font-semibold">Riya</h4>
            <p className="dark:text-gray-600">Designer UX</p>
          </div>
        </div>
      </div>
      <div className="pt-12 border-t dark:border-gray-300">
        <div className="flex flex-col space-y-4 md:space-y-0 md:space-x-6 md:flex-row">
          <img
            src="https://i.ibb.co/PgVX2cN/nafis.jpg"
            alt=""
            className="self-center flex-shrink-0 w-24 h-24 border rounded-full md:justify-self-start dark:bg-gray-500 dark:border-gray-300"
          />
          <div className="flex flex-col">
            <h4 className="text-lg font-semibold">Nafis Arafat</h4>
            <p className="dark:text-gray-600">Application Tester.</p>
          </div>
        </div>
      </div>
    </article>
  );
};

export default IndividualMember;
