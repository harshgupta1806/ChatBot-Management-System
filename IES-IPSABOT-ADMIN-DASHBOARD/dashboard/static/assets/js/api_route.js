// This file will only contain the urls of our api,
// as it is subject to change, and we can't change it in a bunch of files.
const API_BASE_URL = 'http://127.0.0.1:8000';

// END-POINT FOR USERS PAGE
const USERS_EP = API_BASE_URL+'/user';

// END-POINT FOR STUDENTS PAGE
const STUDENTS_EP = API_BASE_URL+'/student';

// END-POINT FOR NOTES PAGE
const NOTES_EP = API_BASE_URL+'/note';

// END-POINT FOR CAMPUS-GUIDE PAGE
const CG_EP = API_BASE_URL+'/cg';

// END-POINT FOR ALERTS PAGE
const ALERTS_EP = API_BASE_URL+'/alert';

// END-POINT FOR RUNsNING SCHEDULERS FOR NOTICE BOARD CHECK
const SCHEDULER_EP = API_BASE_URL+'/check';

export {API_BASE_URL, CG_EP, ALERTS_EP, NOTES_EP, SCHEDULER_EP, STUDENTS_EP, USERS_EP};