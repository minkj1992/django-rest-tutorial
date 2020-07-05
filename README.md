# django-rest-tutorial
Django REST Quickstart tutorial


1. [serialization](https://www.django-rest-framework.org/tutorial/1-serialization/#creating-a-serializer-class): `git tag v1.0.0`
   - Django REST with request binary -> json -> Django.Model -> Django.Model.snippet 연습

2. [Requests and Responses](https://www.django-rest-framework.org/tutorial/2-requests-and-responses/): `git tag v2`
   - Django REST with request and response and url patterns

3. [Views](https://www.django-rest-framework.org/tutorial/3-class-based-views/): `git tag v3`
   - DRY(Don't repeat yourself)
     - FBV -> CBV
   - MIXIN
     - CBV -> MIXIN
   - Generic Class-Based Views
     - MIXIN -> generic class-based views

4. [Authentication & Permissions](https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/): `git tag v4`
   - 코드 스니펫은 항상 제작자와 연결되어 있습니다.
   - 인증된 사용자만 스니펫을 만들 수 있습니다.
   - 스니펫을 만든 사람 만 업데이트하거나 삭제할 수 있습니다.
   - 인증되지 않은 요청에는 전체 읽기 전용 액세스 권한이 있어야합니다.
   - Associating
     1. snippet model
        1. fk field 추가 및 관계/삭제 관리 설정
        2. .save() override하여 필요한 필드 초기화
     2. serializer에 user 클래스 추가
        1. User application단에서 control해주기 위해 serializer단에서도 관계 설정 (views.py에서 관리해주기 위해)
     3. view에 User관련 클래스 추가
     4. url에 user route 등록
     5. fk의 주인인 snippet에서 reverse하게 owner를 field로 가지기 위해 view.SnippetList에 perform_create(owner)추가
     6. snippet_serializer에 ReadOnlyField로 reverse_fk(owner)를 등록
   - Authentication & permission
     1. views의 필요한 클래스들에게 permission_class 필드 등록하여 검사 해주어야 하는 범위 지정
        - 해당 필드를 명시하지 않으면 permission 검사는 지정하지 않게되며 500 HTTP에러와 Django Value Error 메시지가 전달된다. 즉 클라이언트가 예상한 데이터 타입을 return 하지 못했다. 
     2. rest_test 사이트에 로그인/로그아웃 기능이 있는 url추가 (rest_framework.urls)
     3. 소유자와 readOnly데이터에 대해서만 permission-level을 지정하는 custom permission 모듈 생성하여 view-class permission_class에 추가
5. [Relationships & Hyperlinked APIs](https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/): `git tag v5`
   - Post-Redirect-Get pattern은 rest에서 201 Http-status와 `Location` 헤더를 통해서 redirect해주어야 하는 url을 표현한다.
   - Entity간의 관계를 다루는 방법은 많으면, `HyperlinkedModelSerializer`를 사용해서 해당 프로젝트는 관계를 표현하였다.
      - `HyperlinkedIdentityField`: Entity pk
      - `HyperlinkedRelatedField`: relation표현
   - Pagination
   