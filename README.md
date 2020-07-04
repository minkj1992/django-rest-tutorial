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