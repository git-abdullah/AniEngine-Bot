search_query = {
    'query' : '''
            query ($id: Int, $page: Int, $perPage: Int, $search: String) {
                Page (page: $page, perPage: $perPage) {
                    pageInfo {
                        total
                        currentPage
                        lastPage
                        hasNextPage
                        perPage
                    }
                    media (id: $id, search: $search, type: ANIME) {
                        id
                        title {
                            romaji
                        }
                        siteUrl
                    }
                }
            }
            ''',
    'variables' : {
            'search': '',
                'page': 1,
                'perPage': 5
            }
}

get_query = {
    'query': '''
            query ($id: Int) {
                Media(id: $id, type: ANIME) {
                    id
                    title {
                        english
                    }
                    status
                    genres
                    coverImage {
                        medium
                    }
                    episodes
                    description
                    season
                    startDate {
                        year
                        month
                        day
                    }
                siteUrl
                }
            }
    ''',
    'variables': {'id' : ''}
}
