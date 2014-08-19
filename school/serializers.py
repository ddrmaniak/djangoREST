from rest_framework import serializers
from school.models import Teacher, Student
from Accounts.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source='owner.username')
    teachers = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'identifier', 'teachers')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('name',)

    def restore_object(self, attrs, instance=None):
        assert instance is None, '''
            Cannot update teachers with UpdateTeacherSerializer
            '''
        teacher = Teacher(name=attrs['name'])
        return teacher


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'GPA', 'teacher')

    def restore_object(self, attrs, instance=None):
        assert instance is None, '''
            Cannot update students with UpdateStudentSerializer
            '''
        student = Student(name=attrs['name'],
                          GPA=attrs['GPA'],
                          teacher=attrs['teacher'])
        return student
